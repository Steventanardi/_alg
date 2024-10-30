lookup_table = [2**i for i in range(41)]

def power2n_d(n):
    if n < len(lookup_table):
        return lookup_table[n]
    else:
        return 2**n

print('power2n_d(10)=', power2n_d(10))
print('power2n_d(40)=', power2n_d(40)) 
