import sys

input=265149

if len(sys.argv)>1:
    input = int(sys.argv[1])


def brute_force(input):
    loop_stop=15

    x=0
    y=0
    state = 'inc_x'
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    num=1
   
    # Initialize storage for part 2 problem.
    storage = []
    for i in range( 11 ):
        a = []
        for i in range( 11 ) :
            a.append( 0 )
        storage.append( a )

    storage[5][5] = 1

    #for s in storage:
    #    print s

    print('Input:%d'%input)


    actual_x = 5
    actual_y = 5
    
    while( num < input and storage[actual_y][actual_x] < input ):
    
        #print( state, x, y )
    
        loop_stop-=0#1
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


        #location in actual storage lists
        actual_x = 5+x
        actual_y = 5-y

        a = storage[actual_y+1][actual_x+1]
        b = storage[actual_y+1][actual_x-1]
        c = storage[actual_y+1][actual_x]
        d = storage[actual_y][actual_x-1]
        e = storage[actual_y][actual_x+1]
        f = storage[actual_y-1][actual_x+1]
        g = storage[actual_y-1][actual_x]
        h = storage[actual_y-1][actual_x-1]

        #new value.
        storage[actual_y][actual_x]=a+b+c+d+e+f+g+h
      
        #for s in storage:
        #   print s

        num+=1
        #print(num)
        
    return storage[actual_y][actual_x]
###end

x = brute_force(input)

print( 'First Val after input = %d'%(x) )



