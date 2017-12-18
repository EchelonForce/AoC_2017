import sys
    
def main( args ):
    fn = args[0]
    data = []
    with open( fn) as f:
        for line in f:
            data.append(line.strip().split(' '))

    # for d in data:
        # print(d)

    p0 = Program( data, 0 )
    p1 = Program( data, 1 )

    p1.other_guy(p0)
    p0.other_guy(p1)

    while( p0.terminated == False and p1.terminated == False ):
        if( p0.waiting and p1.waiting ):
            print( 'deadlock' )
            p0.terminated = True
            p1.terminated = True
        else:
            p0.run()
            p1.run()

    print( 'p0.sends',p0.sends )
    print( 'p1.sends',p1.sends )
    print( '118618 is too high' )

class Program():
    def __init__( self, instructions, p ):
        self.instructions = instructions
        self.i = 0
        self.p = p
        self.registers = {'p':p}
        self.waiting = False
        self.terminated = False
        self.q = []
        self.sends = 0
        self.other_prog = None

    def other_guy( self, p ):
        self.other_prog = p

    def rx( self ):
        return self.q.pop( 0 )

    def tx( self, val ):
        self.other_prog.q.append( val )
        self.sends += 1

    def run( self ):

        jump = 1
        if( self.i >=0 and self.i < len(self.instructions) ):
            #print(self.i)
            d=self.instructions[self.i]
            #print(d)
            #print(self.registers)
            

            if d[0] == 'set':
                self.registers[d[1]] = self.get_val(d[2])
            elif d[0] == 'mul':
                if d[1] not in self.registers:
                    self.registers[d[1]]=0
                self.registers[d[1]] = self.registers[d[1]] * self.get_val(d[2])
            elif d[0] == 'add':
                if d[1] not in self.registers:
                    self.registers[d[1]]=0
                self.registers[d[1]] = self.registers[d[1]] + self.get_val(d[2])
            elif d[0] == 'mod':
                if d[1] not in self.registers:
                    self.registers[d[1]]=0
                self.registers[d[1]] = self.registers[d[1]] % self.get_val(d[2])
            elif d[0] == 'snd':
                self.tx( self.get_val(d[1]) )
            elif d[0] == 'jgz':
                check = self.get_val(d[1])
                if check > 0:
                    jump = self.get_val(d[2])
            elif d[0] == 'rcv':
                if len(self.q) > 0:
                    val = self.rx()
                    self.registers[d[1]]=val
                    self.waiting = False
                else:
                    self.waiting = True
                    jump = 0

            self.i = self.i+jump
        else:
            self.terminated = True

    def get_val( self, id ):
        val = 0
        try:
            val = int( id )
        except:
            if id not in self.registers:
                self.registers[id]=0
            val = self.registers[id]
        return val

if __name__ == "__main__":
    main(sys.argv[1:])


