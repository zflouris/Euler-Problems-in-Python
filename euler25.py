def number_of_digits(n):
    return len(str(n))

temp=1
a=1
b=1
index=2
while number_of_digits(b)<1000:
    temp=b
    b=a+b
    a=temp
    index+=1
print(index)
