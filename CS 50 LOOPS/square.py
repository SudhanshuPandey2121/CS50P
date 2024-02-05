def main():
  while True:
    n= int(input('What\'s the side of the square do u want?'))
    if(n>0):
      drawsq(n)
      return
  
def drawsq(n):
  for i in range(n):
    for j in range(n):
      print("#",end='')
    print('')
    
main()
