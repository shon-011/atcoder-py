from asyncore import loop


n = int(input())
x = [list(map(int, input().split())) for i in range(n)]

print(x[0][0])