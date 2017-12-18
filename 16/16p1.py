import sys
    
def main( args ):
    fn = args[0]
    with open( fn) as f:
        for line in f:
            data = line.split(',')
    #print(data)

    solve(data,  )

#   print(firewall)

def solve( data,  ):
    programs = list('abcdefghijklmnop')
    print 'input:  '+''.join(programs)

    for instruction in data:
        if instruction[0] == 'x':
            #x5/11
            temp = instruction[1:].strip().split('/')
            a = int(temp[0])
            b = int(temp[1])
            #print( 'Exchange', a, b )
            programs[a],programs[b] = programs[b],programs[a]

        elif instruction[0] == 's':
            #s5
            spin = int(instruction[1:].strip())
            #print( 'Spin', spin )
            spin = 16-spin
            programs = programs[spin:]+programs[:spin]

        elif instruction[0] == 'p':
            temp = instruction[1:].strip().split('/')
            a = programs.index(temp[0])
            b = programs.index(temp[1])
            #print( 'Swap', temp[0], temp[1] )
            programs[a],programs[b] = programs[b],programs[a]
        else:
            raise Exception( 'bad instruction: '+instruction )
        print 'result: '+''.join(programs)

    print 'output: '+''.join(programs)


if __name__ == "__main__":
    main(sys.argv[1:])


