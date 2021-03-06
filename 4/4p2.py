#fn = 'test1.txt'
fn = 'input.txt'

num_valid = 0
num_invalid = 0

def similar( a, b ):
    if len(a) != len(b):
        return False
    if a == b:
        return True
    
    b_temp = b
    for letter in list(a):
        if letter in b_temp:
            b_temp.replace( letter, '', 1 )
        else:
            return False

    return True



with open( fn) as f:

    line_num = 0
    for line in f:
        
        line_num += 1
        valid = True
        tokens = line.split()
        print( line )
        print( tokens )
        for i,t in enumerate(tokens):
            for j,a in enumerate(tokens[i+1:]):
                print( a, t )

                if similar(t,a):
                    print( t+' [%d] is similar to '%(i) + a + ' [%d] in line %d'%( i+j, line_num ) )
                    valid = False
                    num_invalid +=1
                    break
            if not valid:
                break

        if valid:
            num_valid += 1



print( 'num_valid = %d'%num_valid )
print( 'num_invalid = %d'%num_invalid )
print( 'num_lines = %d'%line_num )

