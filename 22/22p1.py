import sys
fn = 'input.txt'

class Node:
    def __init__( self, x, y, val ):
        self.x = x
        self.y = y
        self.val = val
    
    def __repr__( self ):
        return '[%d, %d]=#'%(self.x,self.y)
        
def main():
    #data = []
    infected = []
    with open(fn, 'r') as f:
        y = 0
        for line in f:
            x = 0
            for m in line:
                if '#' == m:
                    #data.append( Node( x, y, True ) )
                    infected.append( Node( x,y, True) )
                #if '.' == m:
                    #data.append( Node( x, y, False ) )
                x += 1
            y+=1
            
    run( infected, x/2, y/2 )

def find( data, x, y ):
    for d in data:
        if d.x ==x and d.y == y:
            return d
    return None
      
def run( infected, mid_x, mid_y ):      

    iterations = 10000
    num_infections = 0
    dir = 'u'
    cur_x = mid_x
    cur_y = mid_y
    prev = find( infected, cur_x, cur_y )
    for i in range( iterations ):
        #print( 'iteration', i )
        #print( 'cur_x', cur_x )
        #print( 'cur_y', cur_y )
        #print( 'prev', prev )
        #print( 'dir', dir )
        if prev is None:
            infected.append( Node( cur_x, cur_y, True) )
            num_infections+=1
            if dir == 'u':
                dir = 'l'
                cur_x = cur_x-1
            elif dir == 'd':
                dir = 'r'
                cur_x = cur_x+1
            elif dir == 'l':
                dir = 'd'
                cur_y = cur_y+1
            elif dir == 'r':
                dir = 'u'
                cur_y = cur_y-1
        else:
            infected.remove( prev )
            if dir == 'u':
                dir = 'r'
                cur_x = cur_x+1
            elif dir == 'd':
                dir = 'l'
                cur_x = cur_x-1
            elif dir == 'l':
                dir = 'u'
                cur_y = cur_y-1
            elif dir == 'r':
                dir = 'd'
                cur_y = cur_y+1

        prev = find( infected, cur_x, cur_y )

    print( 'num_infections', num_infections )
    #print_infected( infected )
    
def print_infected( data ):
    min_x = min( [ a.x for a in data ])
    min_y = min( [ a.y for a in data ])
    dims_x = max( [ a.x for a in data ])+1
    dims_y = max( [ a.y for a in data ])+1
    for y in range( min_y, dims_y ): 
        l = ''
        for x in range( min_x, dims_x ):       
            node = find( data, x, y )
            if node is not None:
                l += '#'
            else: 
                l += '.'
        print( l )
    
if __name__ == "__main__":
    main()    
    
    
    
    
    