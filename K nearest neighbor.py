x=[(2,8),(4,10),(6,12),(8,14),(10,16)]
k = 3
c1=(7,19)
flag=True
dis=[]
for i in range(len(x)):
    cluster1=abs(c1[0]-x[i][0])+abs(c1[1]-x[i][1])
    t=(i,cluster1)
    dis.append(t)
print("Centeriod Cluster:",c1)
print("\nPoint\t\t\tDistance")
for i in range(len(x)):
    print(x[i],"\t\t",dis[i][1])

for i in range(len(dis)):
 min_idx = i
 for j in range(i+1, len(dis)):
  if dis[min_idx][1] > dis[j][1]:
   min_idx = j
 dis[i], dis[min_idx] = dis[min_idx], dis[i]

y=0
z=0
print("\n3 nearest neighbours of centeriod:")
for i in range(k):
    t=dis[i][0]
    print(x[t])
    y=y+x[t][0]
    z=z+x[t][1]

c1 =(round(y/k),round(z/k))   
print('\nUpdated Centeriod:',c1)

