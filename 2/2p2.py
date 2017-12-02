#fn = 'test1.txt'
fn = 'input.txt'
total = 0

with open( fn) as f:
    for line in f:
        nums = [ int(s) for s in line.split() ]
        for n in nums:
            for m in nums:
                if n>m and n%m==0:
                    total = total + (n/m)
               
print( total )
