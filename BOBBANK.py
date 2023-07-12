# cook your dish here
t=int(input())
for i in range(t):
    (w,x,y,z)=map(int, input().split())
    amt_remain=x-y
    final=w+amt_remain*z
    print(final)
    