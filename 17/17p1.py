skip = 316

buf = [0]

top = 2017

buf_pos = 0

for i in range( 1, top+1 ):
    buf_pos = ((skip+buf_pos)%len(buf))+1
    buf.insert(buf_pos,i)

print( buf[buf.index(top)+1] )