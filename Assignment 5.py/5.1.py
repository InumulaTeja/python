l,r=map(int,input().split(" "))
maxm = -1
for  i in range(l,r+1):
    for j in range(l,r+1):
        maxm = max(maxm, i^j)

print(maxm)

