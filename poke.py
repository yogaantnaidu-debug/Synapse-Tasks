import itertools
Pokedex = {
"Pikachu": ("Electric",),
"Charizard": ("Fire", "Flying",),
"Lapras": ("Water", "Ice",),
"Machamp": ("Fighting",),
"Mewtwo": ("Psychic", "Fighting",),
"Hoopa": ("Psychic", "Ghost", "Dark",),
"Lugia": ("Psychic", "Flying", "Water",),
"Squirtle": ("Water",),
"Gengar": ("Ghost", "Poison",),
"Onix": ("Rock", "Ground",)
}

k = int(input("Enter the team size:",))
print("⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄")
allp=list(Pokedex.values())
allpoke=list(itertools.combinations(allp,k))
for i in range(0,len(allpoke)):
    print(allpoke[i])
print("Total possibilities are:",len(allpoke))
print("⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄")
teams = list(Pokedex.keys())
final=[]
maximum=0
subpoke=list(itertools.combinations(teams,k))
for i in range(0,len(subpoke)):
     pika=subpoke[i]
     t=set()
     
     for j in pika:
          t.update(Pokedex[j])
          
          if(len(t)>maximum):
                maximum=len(t)
                final=[(pika,t)]
          elif(len(t)== maximum):
                final.append((pika,t))
          
print("The Strongest Possible teams are:")
for i in range(0,len(final)):
     print(final[i])
print("⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄⚡🔥💧🍃👊👻❄")


            

