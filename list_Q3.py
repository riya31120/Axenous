list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
M = 2
print ("List is: ", list)
print("The following nos. are divisible by 2 ")
for count, num in enumerate(list):
	if( num%M==0) :
		print("Number {0} is at position {1} ".format(num,count))