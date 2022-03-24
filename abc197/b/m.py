H,W,X,Y = map(int, input().split())
counter = 0

hoge = []
for x in range(H):
    hoge.append(input())

for i in range(1,H):
    if 0<=X+i<H:
        if hoge[X+i][Y] == "#":
            break
        else:
            counter+=1

for i in range(1,H):
    if 0<=x-1<H:
        if hoge[X-i][Y] == "#":
            break
        else:
            counter += 1

for i in range(1,W):
    if 0<=Y+1<W:
        if hoge[X][Y+i] == "#":
            break
        else:
            counter+=1

for i in range(1,W):
    if 0<=Y<W:
        if hoge[X][Y-1] == "#":
            break
        else:
            counter += 1


print(counter+1)