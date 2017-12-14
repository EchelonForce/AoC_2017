import re
import sys
    
def main( args ):
    fn = args[0]
    data = {}
    pattern = '(?P<node>[0-9]+) <-> (?P<list>.*)'
    pat = re.compile( pattern )
    with open( fn) as f:
        for line in f:
            m = pat.match(line.strip())
            if m:
                node= m.group('node').strip()
                list = [a.strip() for a in m.group('list').split(',')]
                data[node] = {'children':list, 'in_group':False }
            else:
                raise Exception( 'pattern error' )

    groups = []
    for n in data:
        if not data[n]['in_group']:
            group = get_group(n,data)
            for g in group:
                data[g]['in_group']=True
            groups.append(group)

    print( 'num groups = ', len(groups) )

#print(  )

def get_group( node, data ):    
    cond = [node]
    #for c in data['0']['children']:
    #    cond.append(c)

    for n in data:
        if node in data[n]['children']:
            cond.append( n )
    
    prev_len = 0

    while( len(cond) != prev_len ):
        start_check = prev_len
        prev_len = len(cond)
        for n in cond[start_check:]:
            print( 'checking'+n, prev_len )
            for c in data[n]['children']:
                if c not in cond:
                    cond.append(c)

    return cond

#    print( len(cond) )
            

   # while(len(nodes_to_check)>0):
   #     node_to_check = nodes_to_check[0]
   #     for child in data[node_to_check]:
   #         if child not in nodes_checked:


### main()


##this wont work. need to build a tree and attach trees to nodes or somethign..

def connected( node, data ):
    if data[node]['connected']:
        return True
    else:
        con = False
        for child in data[node]['children']:
            if connected( child ):
                con = True
            if child == '0':
                con = True
        if con:
            for child in data[node]['children']:
                data[child]['connected'] = True
            data[node] = True


if __name__ == "__main__":
    main(sys.argv[1:])


