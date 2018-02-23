a=(input())
print(a)
g=["A","E","I","O","U","a","e","i","o","u"]

if(a in g):
  print("Vowel")
elif a.isalpha():
  print("Consonant")
else:
  print("invalid")
 
