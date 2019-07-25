k1,k2=list(map(int,input().split()))
k3=int(k2)
while k3>0:
  if (k1%k3==0 and k2%k3==0):
    print(k3)
    break
  k3-=1
