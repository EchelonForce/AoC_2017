
import sys

print( 'sys.argv = ', sys.argv )
fn = sys.argv[1]

data = ''
with open( fn) as f:
    for line in f:
        data += line.strip()

#data= data.split(',')
print( data )

lengths = [ord(a) for a in data ]
suffix = [17, 31, 73, 47, 23]
for s in suffix:
    lengths.append(s)

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

for a in range(64):
    for length in lengths:
        
        print( 'position=', position )
        print( 'skip=', skip )
        print( 'length=', length )
        seg_reverse( position, length, buf )
        position += skip+length
        position = (position%len(buf)) 
        skip+=1
        print( 'buf=', buf )
    
my_hash = []

for i in range(16):
    my_hash.append(0)
    for j in range(16):
        my_hash[i] ^= buf[i*16+j]

print( 'my_hash= ', my_hash )

hex_hash = ''
for h in my_hash:
    hex_hash += '%02x'%(h)
print( 'my_hash= 0x', hex_hash )


print( 'buf[0]*buf[1]=%d'%( buf[0]*buf[1] ) )

