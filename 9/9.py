
import sys

print( 'sys.argv = ', sys.argv )
fn = sys.argv[1]

data = ''
with open( fn) as f:
    for line in f:
        data += line

data= data.strip()

data = list(data)
print( 'data=', data )

opened = 0
closed = 0

in_garbage = False
negated = False

score = 0

for i,a in enumerate(data):

    if negated:
        negated = False
        continue

    if '!' == a:
        negated = True
        continue
        
    if '<' == a and not in_garbage:
        in_garbage = True
        continue

    if '>' == a:
        in_garbage = False
        continue

    #print a

    if not in_garbage:
        if '{' == a:
            opened+=1
        if '}' == a:
            score+=opened
            opened-=1
            closed+=1
        

print('opened = %d'%(opened))
print('closed = %d'%(closed))

print('score = %d'%(score))

