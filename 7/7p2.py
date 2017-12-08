
import re

#fn = 'input_test.txt'
fn = 'input.txt'

data = {}

with open( fn) as f:
    pattern_a = '(?P<name>.*) \((?P<weight>.*)\)' 
    pattern_b = '(?P<name>.*) \((?P<weight>.*)\) -> (?P<children>.*)'
    pa = re.compile(pattern_a)
    pb = re.compile(pattern_b)
    for line in f:
        mb = pb.match(line)
        if mb:
            name = mb.group('name')
            weight = mb.group('weight')
            children = mb.group('children' ).split(', ')
            data[name]={'weight':weight, 'children':children}
        else:
            ma = pa.match(line)
            if ma:
                name = ma.group('name')
                weight = ma.group('weight')
                children = None
                data[name]={'weight':weight, 'children':children}
            else:
                print( line, 'doesn\'t match regex' )

# look for root node, which is the child of none
bottom = None
for d in data:
    root = True
    for p in data:
        if d != p:
            if data[p]['children'] is not None:
                if d in data[p]['children']:
                    #print( d, ' is in ', p )
                    root = False
                    break

    if root:
        bottom = d
        break

#for d in data:
#    print( d, data[d] )

# recursive weight calc
def weight( node, data ):
    w = int(data[node]['weight'])
    if data[node]['children'] is not None:
        for c in data[node]['children']:
            w += weight( c, data )
    return w


# find the unbalanced node.
def find_unbalanced( node, data ):
    w = int(data[node]['weight'])
    total_w = w
    balanced = True

    if data[node]['children'] is not None:
        weights = []
        ch_names = []
        for c in data[node]['children']:
            cw, cb = find_unbalanced( c, data )
            weights.append(cw)
            ch_names.append(c)
            total_w+=cw
            if not cb:
                balanced = False
                break

        #count occurences of weights
        cnts = {}
        for a in weights:
            if a in cnts:
                cnts[a] += 1
            else:
                cnts[a]=1
        
        #print( 'cnts', cnts )

        #if there's more than one in the dict, this is unbalanced.
        if len(cnts) > 1:
            balanced = False
            unbalanced_cnt = 0
            for c in cnts:
                if cnts[c] == 1:
                    unbalanced_cnt = c
                    break

            #get index in weights of odd one out.
            unbalanced_idx = None
            for i,a in enumerate(weights):
                if a == unbalanced_cnt:
                    unbalanced_idx = i


            print( 'node '+node+' is unbalanced' )
            print( 'unbalanced_idx = %d'%unbalanced_idx)
            print( 'unbalanced_node = %s'%ch_names[unbalanced_idx])
            print( 'unbalanced_node_weight = %d'%weights[unbalanced_idx])
            print( 'weights = ')
            print( weights )
            print( 'diff=%d'%(max(weights)-min(weights)))
            print( 'node\'s weight=%d', data[ch_names[unbalanced_idx]]['weight'])
            exit()
            #print( '\n\n' )
    return total_w, balanced




weight, balanced = find_unbalanced( bottom, data )



#print( 'root weight', weight( 'ugml', data) )
#print( '\n\n bottom: '+bottom )    
