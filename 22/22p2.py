import sys
fn = 'input-test.txt'

class Node:
    def __init__( self, x, y, val ):
        self.x = x
        self.y = y
        self.val = val
    
    def __repr__( self ):
        return '[%d, %d]=#'%(self.x,self.y)
        
class Sparse2D:
    def __init__( self ):
        self.ys = {}
        self.min_x = 1
        self.min_y = 1
        self.max_x = -1
        self.max_y = -1
    
    def append( self, node ):
        self.min_max( node.x,node.y )
        if node.y in self.ys:
            self.ys[node.y].append(node)
        else:
            self.ys[node.y] = [node]

    def find( self, x, y ):
        nodes = self.ys.get(y)
        if nodes is not None:
            for n in nodes:
                if n.x == x:
                    return n
        return None
     
    def remove( self, node ):
        nodes = self.ys.get(node.y)
        nodes.remove( node )
        if len(nodes)==0:
            self.pop(y)

    def min_max(self, x, y):
        self.min_x = min(self.min_x, x)
        self.min_y = min(self.min_y, y)
        self.max_x = max(self.max_x, x)
        self.max_y = max(self.max_y, y)

    def print_infected( self ):
        print( '-----' )
        for y in range( self.min_y, self.max_y ): 
            l = ''
            for x in range( self.min_x, self.max_x ):       
                node = self.find( x, y )
                if node is not None:
                    l += node.val
                else: 
                    l += '.'
            print( l )
        print( '-----' )

def main( args ):
    #data = []
    fn = args[0]
    infected = Sparse2D()
    with open(fn, 'r') as f:
        y = 0
        for line in f:
            x = 0
            for m in line:
                if '#' == m:
                    #data.append( Node( x, y, True ) )
                    infected.append( Node( x,y, 'i') )
                #if '.' == m:
                    #data.append( Node( x, y, False ) )
                x += 1
            y+=1
            
    run( infected, x/2, y/2 )

# def find( data, x, y ):
    # for d in data:
        # if d.x ==x and d.y == y:
            # return d
    # return None
      
def run( infected, mid_x, mid_y ):      

    iterations = 1000
    num_infections = 0
    dir = 'u'
    cur_x = mid_x
    cur_y = mid_y
    prev = infected.find( cur_x, cur_y )
    for i in range( iterations ):
        if i%10000==0:
            print( 'iteration', i )
            print( 'len(infected)', len(infected.ys) )
            
        #print( 'cur_x', cur_x )
        #print( 'cur_y', cur_y )
        #print( 'prev', prev )
        #print( 'dir', dir )
        #Clean nodes become weakened.
        #If it is clean, it turns left.
        if prev is None:
            infected.append( Node( cur_x, cur_y, 'w') )
            #If it is clean, it turns left.
            if dir == 'u':
                dir = 'l'
            elif dir == 'd':
                dir = 'r'
            elif dir == 'l':
                dir = 'd'
            elif dir == 'r':
                dir = 'u'
        #Weakened nodes become infected.
        elif prev.val == 'w':
            #If it is weakened, it does not turn, and will 
            #continue moving in the same direction.
            prev.val = 'i'
            num_infections+=1
                
        #Flagged nodes become clean.
        elif prev.val == 'f':
            #If it is flagged, it reverses direction, 
            #and will go back the way it came.
            if dir == 'u':
                dir = 'd'
            elif dir == 'd':
                dir = 'u'
            elif dir == 'l':
                dir = 'r'
            elif dir == 'r':
                dir = 'l'
            infected.remove( prev )

        #Infected nodes become flagged.
        elif prev.val == 'i':
            prev.val = 'f'
            #If it is infected, it turns right.
            if dir == 'u':
                dir = 'r'
            elif dir == 'd':
                dir = 'l'
            elif dir == 'l':
                dir = 'u'
            elif dir == 'r':
                dir = 'd'
            
        #move
        if dir == 'u':
            cur_y = cur_y-1
        elif dir == 'd':
            cur_y = cur_y+1
        elif dir == 'l':
            cur_x = cur_x-1
        elif dir == 'r':
            cur_x = cur_x+1

        prev = infected.find( cur_x, cur_y )

    infected.print_infected( )
    print( 'num_infections', num_infections )
    
    

if __name__ == "__main__":
    main(sys.argv[1:])   
    
    
    
    
    