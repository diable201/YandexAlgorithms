a = int(input())
b = int(input())
c = int(input())
if a == b == c == 0:
    print("MANY SOLUTIONS")
elif c < 0:
    print("NO SOLUTION")
else:
    if a != 0:
        ans = int((c ** 2 - b) / a)
        if a * ans + b == c ** 2:
            print(ans)  
        else:
            print("NO SOLUTION")
    elif a == 0 and b == c ** 2:
        print("MANY SOLUTIONS")
    else:
        print("NO SOLUTION")