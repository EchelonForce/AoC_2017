import sys
import re

class Particle():

    def __init__(self, line, i ):
        pattern = 'p=<(?P<pos>[ 0-9-,]*)>, v=<(?P<vel>[ 0-9-,]*)>, a=<(?P<acc>[ 0-9-,]*)>'
        pat = re.compile(pattern)
        m = pat.match(line)
        self.pos = []
        self.vel = []
        self.acc = []
        self.i = i
        if m:
            self.pos = [int(a) for a in m.group('pos').split(',')]
            print self.pos
            self.vel = [int(a) for a in m.group('vel').split(',')]
            print self.vel
            self.acc = [int(a) for a in m.group('acc').split(',')]
        else:
            raise Exception( 'bad line %s'%line )
        pass

        self.dist = sum( [abs(p) for p in self.pos] )

        self.collided = False
        print( self )

    def run( self ):
        self.vel = [ v+a for v,a in zip( self.vel, self.acc ) ]
        self.pos = [ p+v for p,v in zip( self.pos, self.vel ) ]

        self.dist = sum( [abs(p) for p in self.pos] )
        #print('self.dis',self.dist)
        #print('self.pos',self.pos)
        #print('self.vel',self.vel)
        #print('self.acc',self.acc)
    
    def __str__( self ):
        s = '[%d] '%self.i
        s+='p=<%d,%d,%d>, v=<%d,%d,%d>, a=<%d,%d,%d>'%(tuple(self.pos)+ tuple(self.vel)+ tuple(self.acc))
        return s


def main( args ):
    fn = args[0]
    data = []
    with open( fn) as f:
        i = 0
        for line in f:
            p = Particle( line, i )
            data.append(p)
            i = i+1
            #print( p )
    print( 'starting point cnt = %d'%len(data) )
    run( data )

def run (data):
    
    last_i = 0
    min_i = 0
    min_dist = 10000

    dists = []
    for i,p in enumerate(data):
        dists.append(p.dist)
    
    collisions = check_collisions( data )
    if collisions:
        remove_collisions( data )

    min_dist = min( dists )
    min_i = dists.index(min_dist)

    cnt = 0
    while cnt < 1000: 

        for p in data:
            p.run()

        #print( dists )
        collisions = check_collisions( data )

        if not collisions:
            cnt+=1
        else:
            remove_collisions( data )
            cnt = 0
    
    a = 0
    for i,p in enumerate(data):
        if not p.collided:
            a+=1
    print( 'num not collided', a )

def remove_collisions( data ):
    for i,p in enumerate(data):
        if( p.collided ):
            data.pop(i)

def check_collisions( data ):
    got_collision = False
    for i,p in enumerate(data):
        for j,d in enumerate(data[i+1:]):
            if p.pos[0]==d.pos[0] and p.pos[1]==d.pos[1] and p.pos[2]==d.pos[2]:
                #print( p )
                #print( d )
                print( i, i+j, 'collided' )
                p.collided = True
                d.collided = True
                got_collision = True
            else:
                #print('no colision')
                pass
    #print('--------------------------------------------------------------')
    return got_collision

if __name__ == "__main__":
    main(sys.argv[1:])