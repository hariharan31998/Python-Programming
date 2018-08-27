a=int(input())
b=int(input())
f=0
for i in range(0,100):
  if((b**i)==a):
    f=1;
if(f==1):
  print("yes")
else:
  print("no")
