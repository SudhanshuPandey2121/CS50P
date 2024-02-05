import sys
'''
for i in sys.argv:
  print('Hello my dear friend ',i)
  #the above command produces 4 name tags when we want 3 this can be
  # prevented by using Slices
  '''
for i in sys.argv[:-1]:
  print('Hello my dear friend ',i)
