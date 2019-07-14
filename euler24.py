from math import factorial

def max(n,m):
    f=factorial(m)
    return (n%f,int(n/f))

ls=list(range(10))
result=""
n=9
N=(10**6-1,0)
while n>=0:
    N=max(N[0],n)
    result=result+str(ls.pop(N[1]))
    n-=1
print(result)
