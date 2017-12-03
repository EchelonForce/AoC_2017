import sys

input=265149

if len(sys.argv)>1:
    input = int(sys.argv[1])

def brute_force(input):

    x=0
    y=0
    state = 'inc_x'
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    f=1
    print(input)
    while( f < input ):
    
        print( state, x, y )
    
        if( state == 'inc_x' ):
            x+=1
            if( x>max_x ):
                state = 'inc_y'
                max_x=x

        elif( state == 'inc_y' ):
            y+=1
            if( y>max_y ):
                state = 'dec_x'
                max_y=y

        elif( state == 'dec_x' ):
            x-=1
            if( x<min_x ):
                state = 'dec_y'
                min_x=x
    
        elif( state == 'dec_y' ):
            y-=1
            if( y<min_y ):
                state = 'inc_x'
                min_y=y
        f+=1
        print(f)
        
    return (x,y)
    ###end

x,y = brute_force(input)

print( 'x = %d, y = %d, sum = %d'%(x,y,abs(x)+abs(y)) )



