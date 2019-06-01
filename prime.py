def prime(n):
    a=(n//2)
    c=0
    for b in range(2,a+1):
        if (n%b==0):
            c=1
            return c
        else:
            return c
            
    
n=int(input("Enter the prime number to check: "))
print(n)
c=prime(n)
print(c)
if(c==0):
    print("Prime number")
else:
    print("Not a prime number")
