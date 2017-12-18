import sys
    
def main( args ):
    """ This takes the filename.txt instructions and converts them to c calls. Saving them in filename.c_code """
    fn = args[0]
    with open( fn) as f:
        for line in f:
            data = line.split(',')

    with open(fn.replace('txt','c_code'), 'w' ) as out_file:
        generate_c_code( data, out_file )


def generate_c_code( data, out_file ):
    """This translates the input dance moves into c function calls. """
    for instruction in data:
        if instruction[0] == 'x':
            #x5/11
            temp = instruction[1:].strip().split('/')

            c_str = 'exchange( buf, '+temp[0]+', '+temp[1]+' );'
            out_file.write(c_str+'\n')
            
        elif instruction[0] == 's':
            #s5
            spin = instruction[1:].strip()
            
            c_str = 'spin( buf, '+spin+' );'
            out_file.write(c_str+'\n')

        elif instruction[0] == 'p':
            #pa/d
            temp = instruction[1:].strip().split('/')
            
            c_str = 'swap( buf, \''+temp[0]+'\', \''+temp[1]+'\' );'
            out_file.write(c_str+'\n')
        else:
            raise Exception( 'bad instruction: '+instruction )



if __name__ == "__main__":
    main(sys.argv[1:])


