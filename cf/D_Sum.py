
for _ in range(int(input())):
    a,b,c = map(int,input().split())

    if a + b == c or b + c == a or c + a == b:
        print('YES')
    else:
        print('NO')
