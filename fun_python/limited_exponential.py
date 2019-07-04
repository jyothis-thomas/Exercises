#Program to print exponet of a number upto a limit 
#given by the user

import math

#get limit from user
n = int(input("Enter the limit upto which pi is to be printed"))

#limiting the output to 15 digits
if n>15:
	print("Try again with a lower digit")

#round of the exponent and print it
else:
	y = round(math.e,n)
	print(y)