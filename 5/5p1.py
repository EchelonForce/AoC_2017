#fn = 'test1.txt'
fn = 'input.txt'


with open( fn) as f:
    
    data = []
    for line in f:
        data.append( int(line) )

    print( data )

    idx = 0


    cnt = 0
    while( idx < len (data) ):
        jump = data[idx]
        data[idx]+=1
        idx = idx+jump
        cnt+=1

    print( cnt ) 
