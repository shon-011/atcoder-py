n=int(input())
a=n//3600
b=(n%3600)//60
c=n%60
print('{0:02d}:{1:02d}:{2:02d}'.format(a,b,c))