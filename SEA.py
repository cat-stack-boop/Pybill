print('------------------------------------------------\n\
Canberra Snowy hydro Energy \n\
------------------------------------------------')    # New line formating 


previous = input("Enter the previous reading :")       # user enters a number which is saved as a variable 

current = input("Enter the current reading :") 



difference = current - previous                  




if (difference <= 1000):                                 
		amount = difference * 0.15
elif (difference >1000):
	amount = (1000 * 0.15) + (difference - 1000) * 0.25            # need to cut total amount into different tariff brackets 



print('Cheers Mate!')

print('The bill amount is:$') + str(amount) # converting an int to a string



print('Till next time.')