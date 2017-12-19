import sys
    
def main( args ):
    fn = args[0]
    data = []
    with open( fn) as f:
        for line in f:
            data.append([ a for a in line.replace('\n','')])

    for d in data:
        print(d)
        print(len(d))

    run( data )

def run (data):

    max_len = 0
    cols = max( [len(d) for d in data ] )
    rows = len( data )

    print( 'row=%d'%rows)
    print( 'cols=%d'%cols)

    start = data[0].index('|')
    print( 'start=%d'%start)

    pos_x = start
    pos_y = 0

    dir = 'down'
    steps = 0
    letters = []

    while( dir != 'stop' ):
        steps +=1 
        print( 'pos_x=%d'%pos_x)
        print( 'pos_y=%d'%pos_y)

        if dir == 'down':
            next_pos_x = pos_x
            next_pos_y = pos_y+1
        if dir == 'up':
            next_pos_x = pos_x
            next_pos_y = pos_y-1
        if dir == 'left':
            next_pos_x = pos_x-1
            next_pos_y = pos_y
        if dir == 'right':
            next_pos_x = pos_x+1
            next_pos_y = pos_y
        
        print( 'next_pos_x=%d'%next_pos_x)
        print( 'next_pos_y=%d'%next_pos_y)

        next_pos_val = data[next_pos_y][next_pos_x]
        print( 'next_pos_val=%s'%next_pos_val)

        if next_pos_val == '+' :
            if dir == 'down' or dir == 'up':
                if data[next_pos_y][next_pos_x-1] != ' ':
                    dir = 'left'
                elif data[next_pos_y][next_pos_x+1] != ' ':
                    dir = 'right'
            elif dir == 'left' or dir == 'right':
                if data[next_pos_y-1][next_pos_x] != ' ':
                    dir = 'up'
                elif data[next_pos_y+1][next_pos_x] != ' ':
                    dir = 'down'
        elif next_pos_val == ' ':
            dir = 'stop'
        elif next_pos_val not in ['+', '-', '|']:
            letters.append( next_pos_val )

        pos_x = next_pos_x
        pos_y = next_pos_y

    print( 'letters', ''.join(letters) )
    print( 'steps = %d'%steps)

if __name__ == "__main__":
    main(sys.argv[1:])
