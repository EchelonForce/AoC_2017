#original input.
# set b 79
# set c b
# jnz a 2
# jnz 1 5
# mul b 100
# sub b -100000
# set c b
# sub c -17000
# set f 1
# set d 2
# set e 2
# set g d
# mul g e
# sub g b
# jnz g 2
# set f 0
# sub e -1
# set g e
# sub g b
# jnz g -8
# sub d -1
# set g d
# sub g b
# jnz g -13
# jnz f 2
# sub h -1
# set g b
# sub g c
# jnz g 2
# jnz 1 3
# sub b -17
# jnz 1 -23

#Disassemble 1
#set b 79
#set c b
#jnz a 2
#jnz 1 5
#mul b 100      
#sub b -100000  b = 79*100+100000
#set c b        
#sub c -17000   c=b+17000
#    set f 1
#            set d 2
#            set e 2
#                set g d        
#                mul g e        
#                sub g b        g=d*e-b
#                jnz g 2
#                set f 0
#                sub e -1       e=e+1
#                set g e        
#                sub g b        g=e-b
#                jnz g -8
#            sub d -1    d=d+1    
#            set g d     
#            sub g b     g = d-b
#            jnz g -13
#    jnz f 2
#    sub h -1
#    set g b
#    sub g c g=b-c
#    jnz g 2
#    jnz 1 3
#    sub b -17
#jnz 1 -23

#dissemble 2
#b = (79*100)+100000
#c = b+17000
#g=1
#while( g != 0 ):
#    f=1
#    d = 2
#    while g!=0:
#        e = 2
#        while( g!=0 ):
#            print( e,d)
#            if( d*e == b ):
#                f=0
#            if d*e > b: #simplification...
#                break
#            e=e+1
#            g=e-b
#        d=d+1
#        g = d-b
#    if f!=0:
#        h+=1
#        print( h )
#    g=b-c
#    b+=17
#f=1

#Figured out it's basically looking for non-primes.

def isprime(n):
    '''check if integer n is a prime'''

    # make sure n is a positive integer
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2: 
        return True    

    # all other even numbers are not primes
    if not n & 1: 
        return False

    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True

b = (79*100)+100000
c = b+17000+17
a = range( b, c, 17 )
h=0
#print a
for d in a:
    if not isprime( d ):
       h+=1

print( 'non primes = %d'%h )