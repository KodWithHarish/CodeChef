# cook your dish here
t=int(input())
for i in range(t):
    x, y = input().split()
    z=int(x)+int(y)
    if z>6:
        print("YES")
    else:
        print("NO")