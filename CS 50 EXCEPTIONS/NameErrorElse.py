while True:
	try:  
		n=int(input('Whats x?'))
		
	except ValueError:
		print('x not an integer')
	else:
		print(f'x is {n}')
		break  
	 
'''
#when the else statement was not being used and we used only the prinst. 
then valueerror occcured in the second line and nothing got assigned to
n thus a name error occured while we tried to print coz it was an empty 
container to tackle it we used else
'''