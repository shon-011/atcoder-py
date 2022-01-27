a, b, c = map(int, input().split())
n = a*a + b*b 

if n < c*c:
    print('Yes')
else:
    print('No')