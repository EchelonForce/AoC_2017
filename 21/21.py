import sys
import re

class Rule():

    def __init__( self,  line ):

        #parse the input line
        pattern = '(?P<in>[#./]+) => (?P<out>[#./]+)'
        pat = re.compile(pattern)
        m = pat.match(line)
        if m:
            self.input = m.group('in')
            self.output = m.group('out')
        else:
            raise Exception( 'bad line %s'%line )
        pass
        
        #turn the input into a boolean 2d array.
        a = self.input.split('/')
        p = [ [ True if l=='#' else False for l in k ] for k in a ] 
        
        #turn the output into a boolean 2d array.
        b = self.output.split('/')
        self.output_pat =  [ [ True if l=='#' else False for l in k ] for k in b ] 

        #take the input (now in p) and flip/rotate it, creating a list
        #of match-able inputs (in r).
        r = []
        if len(p) == 2:
            a,b = tuple(p[0])
            c,d = tuple(p[1])
            r.append(p) #x1
            r.append([p[1],p[0]]) # x5
            r.append([[c,a],[d,b]]) #x2
            r.append([[d,c],[b,a]]) #x3
            r.append([[b,d],[a,c]]) #x4
            r.append([[a,c],[b,d]]) #x6
            r.append([[b,a],[d,c]]) #x7
            r.append([[d,b],[c,a]]) #x8
        if len(p) == 3:
            a,b,c = tuple(p[0])
            d,e,f = tuple(p[1])
            g,h,i = tuple(p[2])
            r.append(p) #x1
            r.append([p[2],p[1],p[0]]) #x5
            r.append([[g,d,a],[h,e,b],[i,f,c]]) #x2
            r.append([[i,h,g],[f,e,d],[c,b,a]]) #x3
            r.append([[c,f,i],[b,e,h],[a,d,g]]) #x4
            r.append([[c,b,a],[f,e,d],[i,h,g]]) #x6
            r.append([[i,f,c],[h,e,b],[g,d,a]]) #x7
            r.append([[a,d,g],[b,e,h],[c,f,i]]) #x8

        # for t in r:
            # for a in t:
                # print [ '#' if b else '.' for b in a ]
            # print('------------')

        #de-duplicate r and save it in sel.all_pats
        self.all_pats = []
        for p in r:
            add = True
            for p2 in self.all_pats:
                if self.compare(p,p2):
                    add = False
            if add:
                self.all_pats.append( p )

        #print inputs.
        #for t in self.all_pats:
        #    for a in t:
        #        print [ '#' if b else '.' for b in a ]
        #    print('------------')


    def compare(self, pat1, pat2 ):
        """ Compare two 2D patterns """
        #print( 'compare', pat1, pat2 )
        if len(pat1) == len(pat2):
            if( len(pat1) == 3 and pat1[1][1]!=pat2[1][1]):
                return False
                #print( 'nomatch 3x3' )
            for i, x in enumerate(pat1):
                for j, y in enumerate(x):
                    if not pat2[i][j]==y:
                        return False
                        #print( 'nomatch' )
        else:
            return False
            #print( 'nomatch dims' )
        #print( 'match' )
        return True

    def __str__( self ):
        """ Make into a string. Matching original constructor input. """
        s = self.input + ' => ' + self.output
        return s

    def match( self, pattern ):
        """ Compare two 2D patterns """
        for p in self.all_pats:
            # print('---checking----')
            # for a in p:
                # print [ '#' if b else '.' for b in a ]
            # print('---checking----')
            # print('-----against-----')
            # for a in pattern:
                # print [ '#' if b else '.' for b in a ]
            # print('-----against-----')
            if self.compare( p, pattern ):
                return True
       
        return False

 
def main( args ):
    """ Reads puzzle input and generates outputs. """
    fn = args[0]
    rules = []
    with open( fn) as f:
        i = 0
        for line in f:
            r = Rule( line )
            rules.append(r)

    for r in rules:
        print( r )

    iterations = 18

    #  .#.
    #  ..#
    #  ###
    input = [[False,True,False],[False,False,True],[True,True,True]]
    print('---input-----')
    for row in input:
        print [ '#' if b else '.' for b in row ]
    print('---input-----')
    print('---output-----')

    for i in range(iterations):
        print('iteration = %d'%(i+1))
        input = apply_rules( input, rules )

        #print('---output----')
        #for row in input:
        #    print [ '#' if b else '.' for b in row ]
        #print('---output----')

        input = simplify( input )
        #print('---output-simple----')
        #for row in input:
        #    print [ '#' if b else '.' for b in row ]
        #print('---output-simple----')

        print('count_true_pixels = %d'%(count_true_pixels(input)))

    plot_bools(input)

def plot_bools( input ):
    import matplotlib.pyplot as plt
    plt.gray()
    img = [ [0.0 if a else 1.0 for a in row] for row in input ]
    plt.imshow(img)
    plt.show()


def apply_rules( input, rules ):
    """ Apply rules to input, return new output. """
    output = []

    #Determine if we need 2x2 or 3x3 sub-squares
    if len( input ) % 2 == 0:
        skip = 2
    elif len( input ) % 3 == 0:
        skip = 3
    
    i=0
    while i < len( input ):
        j=0
        new_portions = []
        while j < len( input[i] ):
            #make the next sub-square
            if skip == 2:
                portion =[ input[i]  [j:j+skip],
                           input[i+1][j:j+skip] ]
            else:
                portion =[ input[i]  [j:j+skip],
                           input[i+1][j:j+skip],
                           input[i+2][j:j+skip] ]
            #print('---portion-----')
            #for a in portion:
            #    print [ '#' if b else '.' for b in a ]
            #print('---portion-----')

            found_in_rules = False
            for r in rules:
                if r.match( portion ):
                    new_portions.append( r.output_pat )
                    #print('---newportion-----')
                    #print( r)
                    #for a in r.output_pat:
                    #    print [ '#' if b else '.' for b in a ]
                    #print('---newportion-----')
                    
                    found_in_rules = True
                    break
            
            if not found_in_rules:
                raise Exception("NO MATCH") 

            j+=skip #next horizontal sub-square

        output.append(new_portions)
        i+=skip # next vertical set of sub-squares.

    return output    

def simplify( input ):
    """
    Takes a 4D array and simplifies it.
    [[[[ a, b],[c, d]],[[ a, b],[c, d]]],[[[ a, b],[c, d]],[[ a, b],[c, d]]]]
    becomes:
    [[ a, b, a, b],
     [ c, d, c,d ],
     [ a, b, a, b],
     [ c, d, c,d ]]
    """

    #Assume square dimensions
    dim = len(input)*len(input[0][0])
    #initialize output so we can do index assignment
    output = [ [False for b in range(dim)] for a in range(dim)]

    i = 0
    for portions in input:
        j = 0
        for portion in portions:
            k=0
            for row in portion:
                l=0
                for col in row:
                    output[i+k][j+l] = col
                    l+=1
                k+=1
            j+=len(input[0][0]) #Assume square dimensions
        i+=len(input[0][0]) #Assume square dimensions
            
    return output

def count_true_pixels( input ):
    cnt=0
    for row in input:
        for c in row:
            if c:
                cnt+=1
    return cnt

if __name__ == "__main__":
    main(sys.argv[1:])