t=int(input())
for i in range(t):
    (upr,dmg)=map(int, input().split())
    if(dmg<=upr):
        print(dmg)
    else:
        print(upr)