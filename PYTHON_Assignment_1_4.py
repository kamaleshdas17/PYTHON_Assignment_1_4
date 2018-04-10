##Write a Python program to find the volume of a sphere with diameter 12 cm.
##Formula: V=4/3 * π * r3

import math
inp=int(input('Please enter diameter of sphere: '))

def volumeSphere(inp):
	area=((4/3)*math.pi)*inp**3
	##area=((4/3)*3.14159)*input**3
	return area
	
print ('Volume of sphere with diameter {} is : {}'.format(inp,volumeSphere(inp)))

