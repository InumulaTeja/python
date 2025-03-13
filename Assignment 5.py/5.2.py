def halloween(k):
    a=0
    if k%2==0:
        a=int((k/2)*(k/2))
    else :
        a=int((k//2)*(k-(k//2)))
    print(a)

T=int(input("enter the number of testcases"))
for i in range(T):
    k=int(input())
    halloween(k)
