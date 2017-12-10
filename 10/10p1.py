
import sys

print( 'sys.argv = ', sys.argv )
fn = sys.argv[1]

data = ''
with open( fn) as f:
    for line in f:
        data += line.strip()

data= data.split(',')

lengths = [int(a) for a in data ]
buf = range(0,256,1)
print( 'lengths=', lengths )
print( 'buf=', buf )

#lengths = [3,4,1,5]
#buf = [0,1,2,3,4]

def seg_reverse( start, length, buf ):
    if length<=0 or length > len(buf):
        return

    end = start+length-1
    end = end % len(buf)
    
    if( start == end ):
        return

    while( start != end ):
        print( start, end )
        buf[start],buf[end]=buf[end],buf[start]
        start = (start + 1)%len(buf)
        if( start == end ):
            break
        if end == 0:
            end = len(buf)-1
        else:
            end = end - 1
        if( start == end ):
            break
#seg_reverse( 5, 9, buf)

skip = 0
position = 0

for length in lengths:
    
    print( 'position=', position )
    print( 'skip=', skip )
    print( 'length=', length )
    seg_reverse( position, length, buf )
    position += skip+length
    position = (position%len(buf)) 
    skip+=1
    print( 'buf=', buf )

print( 'buf[0]*buf[1]=%d'%( buf[0]*buf[1] ) )

