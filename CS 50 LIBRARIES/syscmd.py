import sys

#print("Hello my name is",sys.argv[1])
try:
  i=int(sys.argv[1])
  print("The table of",i," is: ")
  for j in range(11):
    print(i,'*',j,'=','',i*j)
except IndexError: 
  print('Enter an input after file name:')
  sys.exit("The exit command got called")
 
print("This line will only be printed if the system doesnt exit") 
#sys.argv[i] takes i/p from cmd at the ith loc
#sys.exit helps us exit the program