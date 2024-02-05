#import random
# but if we only want to import the choice function from random then?
from random import choice
head=0
tail=0
for _ in range(10):
  coin=choice(['Heads','Tails'])
  if (coin=='Heads'):
    head=head+1
  else:
    tail=tail+1
print("The total number of heads occured is : "+ str(head))
print("The total number of tails occured is : "+ str(tail))