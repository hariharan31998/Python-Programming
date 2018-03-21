a=int(input())
b=int(input())
print(a,b)
for i in range(a+1,b):
  if((i%2!=0) and (i%3!=0)) or (i==2) or(i==3):
    print(i)
