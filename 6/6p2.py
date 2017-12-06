
start_banks = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4 ]
#start_banks = [0,2,7,0]

def go(input):
    previous=[]
    previous.append(input)   
    cnt = 0
    done = False
    while not done:
        cnt += 1
        cur_banks = previous[-1][:]
        new_banks = balance( cur_banks )
        #print( previous[-1], 'new', new_banks )
        (seen, cnt) =  seen_before( new_banks, previous )
        if seen:
            done = True
            cycles = len(previous)-cnt
        previous.append(new_banks)
    print( cycles )

def balance( banks ):
    m = max(banks)
    idx = 0
    for i,b in enumerate(banks):
        if b == m:
            banks[i]=0
            idx = i
            break
    #print( 'Distributing %d'%(m))
    while m > 0:
        m -= 1
        idx = (idx+1)%len(banks)
        banks[idx]+=1

    return banks

def seen_before( banks, previous ):
    for i,p in enumerate(previous):
        if banks == p:
            print( banks, 'same as', p )
            return True, i
    return False, i


go(start_banks)

