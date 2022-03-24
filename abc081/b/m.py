from itertools import count


n = int(input())
nums = list(map(int, input().split()))
counter = 0
even = True
while even:
    counter += 1
    nums = list(map(lambda x: x/2, nums))
    for i in nums:
        if i % 2 != 0: 
            even = False
            break
        else:
            pass
print(counter-1)