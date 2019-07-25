k1=int(input())
k2=input()
k3=["a","e","i","o","u","A","E","I","O","u"]
k4=k2[: : -1]
for j in k4:
  if (j in k3):
    continue
  print(j,end="")
