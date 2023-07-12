# cook your dish here
t=int(input())
for i in range(t):
    (n,m,k)=map(int, input().split())
    sum=n+k
    if sum <=m:
        print("YES")
    else:
        print("NO")