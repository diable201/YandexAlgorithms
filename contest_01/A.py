a, b = map(int, input().split())
state = str(input())

if state == "heat":
    print(max(a, b))
elif state == "freeze":
    print(min(a, b))
elif state == "auto":
    print(b)
elif state == "fan":
    print(a)