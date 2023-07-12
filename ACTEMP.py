for _ in range(int(input())):
    A,B,C=map(int,input().split());
    if(A<=B and C<=B):
        print("YES")
    else:
        print("NO")