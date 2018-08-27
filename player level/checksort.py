a=int(input())
b=list()
for i in range(0,a):
  d=int(input())
  b.append(d)
c=sorted(b)
if(c==b):
  print("yes")
else:
  print("no") 
