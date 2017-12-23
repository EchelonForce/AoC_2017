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

    while( p0.terminated == False ): 
            p0.run()

    print( 'muls=%d'%p0.muls )

class Program():
    def __init__( self, instructions, p ):
        self.instructions = instructions
        self.i = 0
        self.p = p
        self.registers = {'p':p, 'a':0}
        self.waiting = False
        self.terminated = False
        self.q = []
        self.muls = 0
        self.other_prog = None

    def run( self ):

        jump = 1
        if( self.i >=0 and self.i < len(self.instructions) ):
            #print(self.i)
            d=self.instructions[self.i]
            #print(d)
            #print(self.registers)
            
            if d[0] == 'set':
                self.registers[d[1]] = self.get_val(d[2])
                #print( 'd[%s]=%d'%(d[1],self.registers[d[1]] ))
            elif d[0] == 'mul':
                if d[1] not in self.registers:
                    self.registers[d[1]]=0
                #print( 'd[%s]=%d*%d'%(d[1],self.registers[d[1]],self.get_val(d[2]) ) )
                self.registers[d[1]] = self.registers[d[1]] * self.get_val(d[2])
                #print( 'd[%s]=%d'%(d[1],self.registers[d[1]] ))
                self.muls +=1
            elif d[0] == 'sub':
                if d[1] not in self.registers:
                    self.registers[d[1]]=0
                #print( 'd[%s]=%d-%d'%(d[1],self.registers[d[1]],self.get_val(d[2]) ) )
                self.registers[d[1]] = self.registers[d[1]] - self.get_val(d[2])
                #print( 'd[%s]=%d'%(d[1],self.registers[d[1]] ))
            elif d[0] == 'jnz':
                check = self.get_val(d[1])
                if check != 0:
                    jump = self.get_val(d[2])

            self.i = self.i+jump
        else:
            self.terminated = True
        #print( self.registers )


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


