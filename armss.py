d=int(input())
e=0
f=d
while f>0:
  num=f%10
  e+=num**3
  f//10
if d==e:
  print("yes")
else:
  print("No")
