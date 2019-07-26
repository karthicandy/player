k1,k2=list(map(int,input().split()))
for i in range(1,k1):
  ky=k2**i
  if(k1==ky):
    print("yes")
    break
else:
  print("no")
