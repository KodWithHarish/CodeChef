# cook your dish here
t=int(input())

for i in range(t):
    (lwr, upr, age) = map(int, input().split(' '))
    if age >=lwr and age <= upr:
        print("YES")
    else:
        print("NO")
