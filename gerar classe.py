import pandas as pd
from classe_pokemon import pokemon

pokemons=pd.read_csv("pokemon_data.csv")

poke1=pokemons.iloc[[1]]

l=[]
for i in range (len(poke1.columns)):
    l.append(poke1.iloc[0,i])
print (1)

pokemon1=pokmon(*1)

print (pokemon1.atk)
