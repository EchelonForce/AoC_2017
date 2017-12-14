import sys
import copy

def main( args ):
    fn = args[0]
    data = []
    with open( fn) as f:
        for line in f:
            temp = line.split(':')
            data.append( [ int(a.strip()) for a in temp ] )
    print(data)

    max_layers = 0
    for a in data:
        max_layers = max( max_layers, a[0])

    print( 'max_layers', max_layers )

    firewall = [ {'len':0,'cur_scan':0,'dir':1} for a in range(0,max_layers+1)]

    #print firewall

    for a in data:
        firewall[a[0]]['len'] = a[1]
    

    print firewall
    temp_copy = copy.deepcopy( firewall )
    delay = 0
    caught = True
    while( caught ):
        #cnt+=1
        #print( 'delay = %d'%delay)
        pos = 0
        severity = 0
        
        firewall = copy.deepcopy(temp_copy)

        for f in firewall:
            if f['len'] > 0:
                f['cur_scan'] += f['dir']
                if f['dir'] == 1 and f['cur_scan'] == (f['len']-1):
                    f['dir'] = -1
                elif f['dir'] == -1 and f['cur_scan']==0:
                    f['dir'] = 1

        temp_copy = copy.deepcopy( firewall )
        #print( d, firewall )

        caught = False
        while pos < len(firewall):
            #print( 'pos= %d'%pos)

            if 0 == firewall[pos]['cur_scan'] and firewall[pos]['len']>0:
                #severity += (pos*firewall[pos]['len'])
                caught = True
                break 
                #print( 'severity= %d'%severity)

            pos += 1
            
            for f in firewall:
                if f['len'] > 0:
                    f['cur_scan'] += f['dir']
                    if f['dir'] == 1 and f['cur_scan'] == (f['len']-1):
                        f['dir'] = -1
                    elif f['dir'] == -1 and f['cur_scan']==0:
                        f['dir'] = 1
                    
            #print firewall
        delay += 1

        if delay %1000 == 0:
            print( 'delay = %d'%(delay))
            sys.stdout.flush()
            
    print( 'delay = %d'%(delay))


if __name__ == "__main__":
    main(sys.argv[1:])


