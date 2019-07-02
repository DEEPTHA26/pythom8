starts=1
ends=20
for d in range(starts,ends+1):
  if d>1:
    for n in range(2,d):
      if(d%n)==0:
        break
      else:
        print(d)
