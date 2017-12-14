
class Knot_Hash():
    def __init__( self, data ):
    
        self.lengths = [ord(a) for a in data ]
        suffix = [17, 31, 73, 47, 23]
        for s in suffix:
            self.lengths.append(s)

        self.buf = range(0,256,1)
        self.my_hash = None
        
        #print( 'lengths=', self.lengths )
        #print( 'buf=', self.buf )

        #lengths = [3,4,1,5]
        #buf = [0,1,2,3,4]

    def seg_reverse( self, start, length, buf ):
        if length<=0 or length > len(buf):
            return

        end = start+length-1
        end = end % len(buf)
        
        if( start == end ):
            return

        while( start != end ):
            #print( start, end )
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

    def hash( self ):
        skip = 0
        position = 0

        for a in range(64):
            for length in self.lengths:
                
                #print( 'position=', position )
                #print( 'skip=', skip )
                #print( 'length=', length )
                self.seg_reverse( position, length, self.buf )
                position += skip+length
                position = (position%len(self.buf)) 
                skip+=1
                #print( 'buf=', self.buf )
            
        my_hash = []

        for i in range(16):
            my_hash.append(0)
            for j in range(16):
                my_hash[i] ^= self.buf[i*16+j]

        #print( 'my_hash= ', my_hash )
        self.my_hash = my_hash

        hex_hash = ''
        for h in my_hash:
            hex_hash += '%02x'%(h)
        self.hex_hash = hex_hash
        #print( 'my_hash= 0x', hex_hash )

    #terrible bit count via look up table of hex chars!
    def set_bit_cnt( self ):
        cnt =0
        if self.my_hash is not None:
            for a in self.hex_hash:
                if a in [ 'f' ]:
                    cnt+=4
                if a in [ '7', 'e', 'd', 'b']:
                    cnt+=3
                if a in [ '3','5','6','9','a', 'c']:
                    cnt+=2
                if a in [ '1','2','4','8' ]:
                    cnt+=1
        return cnt      
        
#### end class Knot_Hash

#Compute all hashes. and count the number of set bits in a terrible way.
hashes = []
full_cnt = 0   
for a in range( 0, 128 ):
    input = 'ljoxqyyw-%d'%(a)
    row = Knot_Hash( input )
    row.hash()
    print( input )
    print( row.hex_hash)
    hashes.append(row.hex_hash)
    a = row.set_bit_cnt()
    full_cnt += a
    print( a )

print( 'full_cnt', full_cnt )

# convert to binary-ish
bin_hashes = []
for h in hashes:
    b = bin(int(h, 16))[2:].zfill(128)
    print b
    bin_hashes.append( [ x for x in b ])

#replace '1's with 'a's
length = 128
for x in range( length ):
    for y in range( length ):
        if bin_hashes[x][y] == '1':
            bin_hashes[x][y] = 'a'
    
#recursive replace adjacent with group
def expand_group( x, y, group, hashes ):
    if hashes[x][y] == 'a':
        hashes[x][y] = group
        if( y+1 < length ):
            expand_group( x, y+1, group, hashes )
        if( y-1 >= 0  ):
            expand_group( x, y-1, group, hashes )
        if( x+1 < length ):
            expand_group( x+1, y, group, hashes )
        if( x-1 >= 0 ):
            expand_group( x-1, y, group, hashes )
        
#make sure everything that's 'a' gets a numeric group.
groups = 0
for x in range( length ):
    for y in range( length ):
        if bin_hashes[x][y] == 'a':
            groups += 1
            expand_group( x, y, '%d'%groups, bin_hashes )
       
for h in bin_hashes:       
    print(h)
    
print( 'regions = ', groups )






