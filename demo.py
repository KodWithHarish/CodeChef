for i in range(int(input())):
    (a,b)=map(int,input().split())
    f=100*(a/100)
    s=200*(b/100)
    # print(f)
    # print(s)
    first = 100-f
    second = 200-int(s)
    print(first)
    print(second)
    if first < second:
        print("FIRST")
    elif first == second:
        print("BOTH")
    else:
        print("SECOND")