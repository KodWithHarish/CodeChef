l = list(map(int, input().strip().split()))[:4]

c=0
for i in range(len(l)):
    if l[i]>=10:
        c=c+1
print(c)