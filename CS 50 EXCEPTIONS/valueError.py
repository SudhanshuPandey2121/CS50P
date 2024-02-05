while True:
  try:  
    n=int(input('Whats x?'))
    print(f'x is {n}')
    break
  except ValueError:
    print('x not an integer')
