import sys
    
def main( args ):
    fn = args[0]
    data = []
    with open( fn) as f:
        for line in f:
            data.append(line.strip().split(' '))

    # for d in data:
        # print(d)

    run( data )


def run( data ):

    registers = {}

    sound=None

    i = 0
    while( i >=0 and i < len(data) ):
        print(i)
        d=data[i]
        print(d)
        print(registers)
        jump = 1

        if d[0] == 'set':
            registers[d[1]] = get_val(registers,d[2])
        elif d[0] == 'mul':
            if d[1] not in registers:
                registers[d[1]]=0
            registers[d[1]] = registers[d[1]] * get_val(registers,d[2])
        elif d[0] == 'add':
            if d[1] not in registers:
                registers[d[1]]=0
            registers[d[1]] = registers[d[1]] + get_val(registers,d[2])
        elif d[0] == 'mod':
            if d[1] not in registers:
                registers[d[1]]=0
            registers[d[1]] = registers[d[1]] % get_val(registers,d[2])
        elif d[0] == 'snd':
            if d[1] not in registers:
                registers[d[1]]=0
            sound=get_val(registers,d[1])
            print( 'sound:', sound )
        elif d[0] == 'jgz':
            check = get_val(registers,d[1])
            if check > 0:
                jump = int(d[2])
        elif d[0] == 'rcv':
            check = get_val(registers,d[1])
            if check > 0:
                print( 'recovered:%d'%sound )
                exit()

        i = i+jump


def get_val( registers, id ):
    val = 0
    try:
        val = int( id )
    except:
        if id not in registers:
            registers[id]=0
        val = registers[id]
    return val

if __name__ == "__main__":
    main(sys.argv[1:])


