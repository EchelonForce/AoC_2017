skip = 316

top = 50000000

buf_pos = 0

val_at_pos_one = 0

length = 1

for i in range( 1, top+1 ):

    # print( 'len', len(buf) )
    buf_pos = ((skip+buf_pos)%length)+1
    length = length + 1
    # print( 'buf_pos', buf_pos )
    #buf.insert(buf_pos,i)

    # print( '--------------------------------------------' )
    if( buf_pos == 1):
        val_at_pos_one = i 
        print( '[ 0, %d, ... ]'%( val_at_pos_one ) )
    
print( val_at_pos_one )
