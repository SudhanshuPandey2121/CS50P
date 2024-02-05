def main():
  n=getnumber()
  printm(n)
  
def getnumber():
  while True: 
    n=int(input("whats n?"))
    if n>0:
      return n
    
  
  

def printm(i):
 
    for  _ in range(int(i)):
      print("meow") 
      
main()      