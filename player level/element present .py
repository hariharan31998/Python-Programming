a=list()
n=input()
b=input()
for i in range(0,int(n)):
  d=input()
  a.append(d)
a=''.join(a)
print(a)
if b in a:
  print("Yes")
else:
  print("No")
