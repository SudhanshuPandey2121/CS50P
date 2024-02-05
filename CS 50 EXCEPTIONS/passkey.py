while True:
	try:  
		n=int(input('Whats x?'))
		
	except ValueError:
		pass
	else:
		print(f'x is {n}')
		break  