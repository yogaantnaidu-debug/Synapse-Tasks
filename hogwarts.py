l=input("Enter runes:")
x="LUMOS"
l=l.upper()
k=0
j=set()
bol =False
for i in range (0,len(l)) :
    k=k+1
    for z in range(0, len(x)):
       if(l[i]==x[z] and not bol):
         p=list(l[i])
         j.update(p)
         if(len(j)==5):
               bol=True
               f=k
               break
if(len(j)==5):
  print(f)
else:
    print("-1")

