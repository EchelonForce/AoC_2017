import sys
import re

class Particle():

    def __init__(self, line ):
        pattern = 'p=<(?P<pos>[0-9-,]*)>, v=<(?P<vel>[0-9-,]*)>, a=<(?P<acc>[0-9-,]*)>'
        pat = re.compile(pattern)
        m = pat.match(line)
        self.pos = []
        self.vel = []
        self.acc = []
        if m:
            self.pos = [int(a) for a in m.group('pos').split(',')]
            self.vel = [int(a) for a in m.group('vel').split(',')]
            self.acc = [int(a) for a in m.group('acc').split(',')]
        else:
            raise Exception( 'bad line %s'%line )
        pass

        self.dist = sum( [abs(p) for p in self.pos] )

    def run( self ):
        self.vel = [ v+a for v,a in zip( self.vel, self.acc ) ]
        self.pos = [ p+v for p,v in zip( self.pos, self.vel ) ]

        self.dist = sum( [abs(p) for p in self.pos] )
        #print(self.dist)
        #print(self.pos)
        #print(self.vel)
        #print(self.acc)
    
    def __str__( self ):
        return 'p=<%d,%d,%d>, v=<%d,%d,%d>, a=<%d,%d,%d>'%( tuple(self.pos)+ tuple(self.acc)+ tuple(self.acc))


def main( args ):
    fn = args[0]
    data = []
    with open( fn) as f:
        for line in f:
            
            p = Particle( line )
            data.append(p)
            print( p )
    run( data )

def run (data):
    
    last_i = 0
    min_i = 0
    min_dist = 10000

    dists = []
    for i,p in enumerate(data):
        dists.append(p.dist)
    
    min_dist = min( dists )
    min_i = dists.index(min_dist)

    cnt = 0
    while cnt < 500: 

        for i,p in enumerate(data):
            p.run()
            dists[i] = p.dist
        min_dist = min( dists )
        min_i = dists.index(min_dist)

        #print( dists )

        if min_i == last_i:
            cnt+=1
            #pass
        else:
            last_i = min_i
            cnt = 0
    
    print( 'Particle %d will stay closest to position <0,0,0> in the long term.'%last_i )

if __name__ == "__main__":
    main(sys.argv[1:])