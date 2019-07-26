k1,k2=list(map(int,input().split()))
count=0
for i in range(k1,k2+1):
  y=i**(1/2)
  if y%1==0:
    count+=1
print(count)
