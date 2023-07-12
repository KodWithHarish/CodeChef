t=int(input())
for i in range(t):
    # cook your dish here
    (passenger,people,amt) = map(int, input().split())
    seats = 10 * passenger

    if people <= seats:
        total = people * amt
        print(total)
    else:
        total = seats * amt
        print(total)