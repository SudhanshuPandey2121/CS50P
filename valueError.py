while True:
    try:
      x= int(input('enter x?'))
      print(f'x is {x}')
      break
    except ValueError:
      print("x is not an integer")