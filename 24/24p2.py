import sys
    
class Tree():

    def __init__( self, attached, unattached, remaining, parent ):
        self.attached = attached
        self.unattached = unattached
        self.remaining = remaining
        self.parent = parent
        self.strength = self.attached+self.unattached
        self.sub_trees = []
        self.build()

    def build( self ):
        for i,p in enumerate(self.remaining):
            if self.unattached == p[0]:
                self.sub_trees.append( Tree( p[0], p[1], self.remaining[0:i]+self.remaining[i+1:], self ) )
            elif self.unattached == p[1]:
                self.sub_trees.append( Tree( p[1], p[0], self.remaining[0:i]+self.remaining[i+1:], self ) )

    def max_strength( self ):
        if len( self.sub_trees ) > 0 :
            strengths = [s.max_strength() for s in self.sub_trees ]
        
            return self.strength + max( strengths )
        else:
            return self.strength
    
    def max_length( self ):
        longest = 0
        strength_longest = 0
        for s in self.sub_trees:
            l,s = s.max_length()
            if l > longest:
                longest = l
                strength_longest = s
            elif l == longest and strength_longest < s:
                longest = l
                strength_longest = s

        return longest+1, strength_longest+self.strength

def main( args ):
    fn = args[0]

    peices = []

    with open( fn) as f:
        for line in f:
            peices.append( [ int(a) for a in line.split('/')] )

    print( peices )

    tree = None

    for p in peices:
        p = sorted(p)
        print p

    for i,p in enumerate(peices):
        if 0 == p[0]:
            if tree is None:
                remaining = peices[0:i]+peices[i+1:]
                tree = Tree( p[0], p[1], remaining, parent = None )
            else:
                raise Exception( 'two zeroes' )

    #print( 'strength', tree.max_strength())

    l,s=tree.max_length()
    print( 'longest', l)
    print( 'strength', s)

if __name__ == "__main__":
    main(sys.argv[1:])

