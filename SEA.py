print('------------------------------------------------\n\
Canberra Snowy hydro Energy \n\
------------------------------------------------')

previous = input("Enter the previous reading :")

current = input("Enter the current reading :") 

difference = current - previous                  

if (difference <= 1000):                                 
		amount = difference * 0.15
elif (difference >1000):
	amount = (1000 * 0.15) + (difference - 1000) * 0.25           

print('Cheers Mate!')

print('The bill amount is:$') + str(amount) # converting an int to a string

print('Till next time.')
