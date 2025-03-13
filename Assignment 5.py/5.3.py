def bigisgreat(w):
    c=0
    a=list(w[::-1])
    for i in range(len(a)-1):
        if ord(a[i])>ord(a[i+1]):
            a[i],a[i+1]=a[i+1],a[i]
            break
        else:
            c+=1
    b=''.join(a)
    if c==len(a)-1:
        print("no answer")
    else :
        print(b[::-1])
T=int(input("enter the number of testcases:"))
for i in range(T):
    w=input()
    bigisgreat(w)


