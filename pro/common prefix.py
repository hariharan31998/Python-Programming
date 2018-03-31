a=int(input())
print(a)
c=list()
import os
for i in range(0,a):
  b=str(input())
  c.append(str(b))
print(c)
d=os.path.commonprefix(c)
print(d)
