import math
import sys
    
def main( args ):
    fn = args[0]
    
    path_taken = ''
    with open( fn) as f:
        for line in f:
            path_taken += line.strip()
    
    path_taken = path_taken.split(',')
    
    print( path_taken )
    
    location_x = 0.0
    location_y = 0.0
    max_dist_x = 0.0
    max_dist_y = 0.0
    max_dist = 0.0
    dist = 0.0
    for move in path_taken:
        if move == 'n':
            location_x += 0
            location_y += 1
        elif move == 's':
            location_x += 0
            location_y += -1
        elif move == 'ne':
            location_x += 1.5
            location_y += 0.5
        elif move == 'se':
            location_x += 1.5
            location_y += -0.5
        elif move == 'nw':
            location_x += -1.5
            location_y += 0.5
        elif move == 'sw':
            location_x += -1.5
            location_y += -0.5
    
        dist = min_moves( location_x, location_y )

        if max_dist < dist:
            max_dist = dist
    
    print( 'location_x=%.1f'%(location_x) )
    print( 'location_y=%.1f'%(location_y) )

    print( 'dist=%.1f'%(dist) )
    print( 'max_dist=%.1f'%(max_dist) )
### main()


def min_moves( x, y ):
    a=0.0
    b=0.0

    if abs(x) < 0.01  and abs(y) < 0.01:    
        a = 0.0
    elif abs(x) < 0.01 :    
        a = abs(y)
    elif abs(y) < 0.01 :    
        a = abs(x/1.5)
    elif x > 0:
        a = x/1.5
        if y > 0:
            b = y-a/2
        elif y < 0:
            b = -y-a/2
    elif x < 0:
        a = -x/1.5
        if y > 0:
            b = y-a/2
        if y < 0:
            b = -y-a/2

    #f = x/1.5
    #b = y-f/2
    print( 'a', b )
    print( 'b', b )
    return abs(a+b)


if __name__ == "__main__":
    main(sys.argv[1:])


