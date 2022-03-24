n = int(input())
x = 2025 - n

for i in range(1,10):
   if x%i == 0 and x/i<=9:
    a = str(i)
    b = str(x//i)
    print(f"{a} x {b}") 

