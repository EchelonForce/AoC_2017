
import re
#fn = 'input-test.txt'
fn = 'input.txt'

regs = {}

with open( fn) as f:
    pattern_a = '(?P<reg>[a-z]+) (?P<op1>[a-z]+) (?P<amount1>[-0-9]+) if (?P<reg2>[a-z]+) (?P<op2>[<=>!]+) (?P<amount2>[-0-9]+)' 
    pa = re.compile(pattern_a)
    for line in f:
        #print(line)
        ma = pa.match(line)
        if ma:
            reg = ma.group('reg')
            condition = ma.group('op2').strip()
            cond_reg = ma.group('reg2')
            cond_val = int(ma.group('amount2'))
            change = int(ma.group('amount1'))
            
            if( reg not in regs):
                regs[reg] = 0
            if( cond_reg not in regs):
                regs[cond_reg] = 0
            
            if( ma.group('op1') == 'dec'):
                change = -1*change

            #print(reg)
            #print(change)
            #print(condition)
            #print(cond_reg)
            #print(cond_val)

            if condition == '==':
                if regs[cond_reg] == cond_val:
                    regs[reg]+=change
            elif condition == '>':
                if regs[cond_reg] > cond_val:
                    regs[reg]+=change
            elif condition == '<':
                if regs[cond_reg] < cond_val:
                    regs[reg]+=change
            elif condition == '!=':
                if regs[cond_reg] != cond_val:
                    regs[reg]+=change
            elif condition == '>=':
                if regs[cond_reg] >= cond_val:
                    regs[reg]+=change
            elif condition == '<=':
                if regs[cond_reg] <= cond_val:
                    regs[reg]+=change
            else:
                print('fail', cond_reg, condition, cond_val )

            #print(regs)
        else:
            print( line, 'doesn\'t match regex' )

max_reg = 0
for r in regs:
    if regs[r] > max_reg:
        max_reg = regs[r]

print( 'max_reg=%d'%(max_reg) )


