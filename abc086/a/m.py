a, b = map(int, input().split())
n = a * b % 2

if n == 0:
    print('Even')
else:
    print('Odd')