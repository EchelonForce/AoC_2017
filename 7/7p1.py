
import re
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


# look for root node, which is a child on none
bottom = None
for d in data:
    root = True
    for p in data:
        if d != p:
            if data[p]['children'] is not None:
                if d in data[p]['children']:
                    print( d, ' is in ', p )
                    root = False
                    break

    if root:
        bottom = d
        break

for d in data:
    print( d, data[d] )

print( '\n\n bottom: '+bottom )    
