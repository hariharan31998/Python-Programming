a=int(input())
print(a)
c=0
h=a
for i in range(0,a):
  b=h%10
  c+=b**3
  h=h//10
if(a==c):
  print("yes")
else:
  print("no")
