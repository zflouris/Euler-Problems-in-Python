from sys import argv
import time

def nines(s):
    if s==0:
         return 1
    sum=10**s-1
    return sum

def circle(n):
    for s in range(1000):
        for m in range(10):
            if (10**m)*nines(s)%n==0:
                return s
z=int(argv[1])
max=1
number=-1
start = time.time()
# print(circle(z))
for x in range(1,z):
    if circle(x)>max:
        max=circle(x)
        number=x
end = time.time()
print((number,max))
print(end-start)
