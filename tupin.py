import numpy as np
import math
z=np.array([[1,0,0,0,1,1],
[1,0,1,1,1,0],
[1,1,0,1,1,1],
[1,0,1,1,0,0],
[0,1,0,1,1,0],[1,0,0,1,0,0]])
m=0
mx=0
my=0
c=0
z=z.T
b=int(input("Enter the blast radius:"))
d=math.floor(b/2)
if(b>len(z)):
    print("Bomb larger than Zone")
for i in range(d,len(z)-d):
    for j in range(d,len(z)-d):
        if(z[i][j]==1):
           c=0
           for k in range(i-d,i+d+1):
               for l in range(j-d,j+d+1):
                   if(z[k][l]==1):
                      c=c+1
                        
        if(c>m):
            m=c
            mx=i
            my=len(z)-j-1

       
print(mx,my,m)
