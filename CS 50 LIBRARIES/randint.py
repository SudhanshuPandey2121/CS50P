import random
#can be used in a dice game
print(random.randint(1,6))

#can be used in a card game
card=['queen','ace','joker','spade','diamond']
random.shuffle(card)

for i in range(len(card)):
  print(card[i])
  
for i in card:
  print(i)