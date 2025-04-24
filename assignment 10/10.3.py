import numpy as np
def odd(n,i):
    a = np.zeros((n, n), dtype=int)
    j = 0
    k = n // 2

    for num in range(i, n**2 + i):
        a[j][k] = num
        j1 = (j - 1) % n
        k1 = (k + 1) % n

        if a[j1][k1] == 0:
            j, k = j1,k1
        else:
            j = (j + 1) % n
    return a


n = int(input("Enter a number: "))
if n % 2 != 0:
    a=odd(n,1)
    print(a)
elif n%4==0:
    a=np.arange(1,n**2+1)
    a=a.reshape((n,n))
    for i in range(n):
        a[i][i]=n**2+1-a[i][i];
    i=0
    j=n-1
    while i<n and j>=0:
        a[i][j]=n**2+1-a[i][j];
        i=i+1
        j=j-1
    print(a)
else :
    a=odd(n//2,1)
    b=odd(n//2,n**2//4+1)
    c=odd(n//2,n**2//2+1)
    d=odd(n//2,3*(n**2//4)+1)
