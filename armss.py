n=int(input())
h=0
a=h
while a>0:
  num=a%10
  h+=num**3
  a//10
if n==h:
  print("yes")
else:
  print("No")
