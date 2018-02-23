a=int(input())
b=int(input())
print(a,b)
c=list()
e=0
for i in range(int(a)):
  d=int(input())
  c.append(int(d))
print(c)
for i in range(0,b):
  e=e+c[i]
print(e)
  
