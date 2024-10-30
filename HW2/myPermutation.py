def perm(n):  
    p = []  
    return permNext(n, p)  

def permNext(n, p):  
    if len(p) == n:  
        print(p)  
        return

    for x in range(n):
        if x not in p:  
            p.append(x)  
            permNext(n, p)  
            p.pop()  

perm(2)  
perm(3)  
perm(4)  
perm(5)  