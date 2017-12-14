import sys
    
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
    pos = 0

    severity = 0

    while pos < len(firewall):
        
        print( 'pos= %d'%pos)

        if 0 == firewall[pos]['cur_scan']:
            severity += (pos*firewall[pos]['len'])
            print( 'severity= %d'%severity)

        pos += 1
        
        for f in firewall:
            if f['len'] > 0:
                f['cur_scan'] += f['dir']
                if f['dir'] == 1 and f['cur_scan'] == (f['len']-1):
                    f['dir'] = -1
                elif f['dir'] == -1 and f['cur_scan']==0:
                    f['dir'] = 1
                
        #print firewall

    print( 'pos%d'%pos)
    print( 'severity%d'%severity)
#   print(firewall)


if __name__ == "__main__":
    main(sys.argv[1:])


