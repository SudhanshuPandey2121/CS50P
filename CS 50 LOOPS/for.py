# can use a underscore if variable not intended to be used in future
'''
for _ in [5,6,8]:
  print('meow')

for i in range(10):
  print('meow')  
 '''
print("meow\n"*3,end="")
  
s=[1,2,3,4]

for i in range(len(s)):
  print((i+1),s[i])
