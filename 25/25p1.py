import sys


def main( args ):

    #Begin in state A.
    #Perform a diagnostic checksum after 12629077 steps.

    state = 'A'
    steps = 12629077
    tape = { 0:0 }
    index = 0
    for i in range( steps ):
        if i % 1000 ==0  and i != 0:
            print( i )

        if state == 'A':
            #In state A:
            #  If the current value is 0:
            #    - Write the value 1.
            #    - Move one slot to the right.
            #    - Continue with state B.
            #  If the current value is 1:
            #    - Write the value 0.
            #    - Move one slot to the left.
            #    - Continue with state B.
            if( tape[index] == 0 ):
                tape[index] = 1
                index+=1
                state = 'B'
            else:
                tape[index] = 0
                index-=1
                state = 'B'

        elif state == 'B':
            #In state B:
            #  If the current value is 0:
            #    - Write the value 0.
            #    - Move one slot to the right.
            #    - Continue with state C.
            #  If the current value is 1:
            #    - Write the value 1.
            #    - Move one slot to the left.
            #    - Continue with state B.

            if( tape[index] == 0 ):
                tape[index] = 0
                index+=1
                state = 'C'
            else:
                tape[index] = 1
                index-=1
                state = 'B'

        elif state == 'C':
            #In state C:
            #  If the current value is 0:
            #    - Write the value 1.
            #    - Move one slot to the right.
            #    - Continue with state D.
            #  If the current value is 1:
            #    - Write the value 0.
            #    - Move one slot to the left.
            #    - Continue with state A.
            if( tape[index] == 0 ):
                tape[index] = 1
                index+=1
                state = 'D'
            else:
                tape[index] = 0
                index-=1
                state = 'A'
        elif state == 'D':
            #In state D:
            #  If the current value is 0:
            #    - Write the value 1.
            #    - Move one slot to the left.
            #    - Continue with state E.
            #  If the current value is 1:
            #    - Write the value 1.
            #    - Move one slot to the left.
            #    - Continue with state F.
            if( tape[index] == 0 ):
                tape[index] = 1
                index-=1
                state = 'E'
            else:
                tape[index] = 1
                index-=1
                state = 'F'
        elif state == 'E':

            #In state E:
            #  If the current value is 0:
            #    - Write the value 1.
            #    - Move one slot to the left.
            #    - Continue with state A.
            #  If the current value is 1:
            #    - Write the value 0.
            #    - Move one slot to the left.
            #    - Continue with state D.
            if( tape[index] == 0 ):
                tape[index] = 1
                index-=1
                state = 'A'
            else:
                tape[index] = 0
                index-=1
                state = 'D'

        elif state == 'F':

            #In state F:
            #  If the current value is 0:
            #    - Write the value 1.
            #    - Move one slot to the right.
            #    - Continue with state A.
            #  If the current value is 1:
            #    - Write the value 1.
            #    - Move one slot to the left.
            #    - Continue with state E.
            if( tape[index] == 0 ):
                tape[index] = 1
                index+=1
                state = 'A'
            else:
                tape[index] = 1
                index-=1
                state = 'E'

        if index not in tape:
            tape[index] = 0

    cnt = 0
    for i in tape:
        if tape[i] == 1:
            cnt+=1


    print('set bits', cnt )


if __name__ == "__main__":
    main(sys.argv[1:])

