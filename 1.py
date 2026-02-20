def func(n):
    if n==0 or n==1:
        return n
    else:
        f0=0
        f1=1
        f=-1
        for i in range(2,n+1):
            f=f0+f1
            f0=f1
            f1=f
        return f
    
n=int(input())
print(func(n))
