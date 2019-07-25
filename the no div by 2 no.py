k1,k2=list(map(int,input().split()))
k3=1
while k3>0:
  if(k3%k1==0 and k3%k2==0):
    print(k3)
    break
  k3+=1
