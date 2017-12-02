fn = 'input.txt'

checksum = 0

with open( fn) as f:
    for line in f:
        nums = [ int(s) for s in line.split() ]
        
        checksum = checksum + max(nums) - min(nums)
        
        
print( checksum )
