 # /**************************************************** 
 #  *  Problem : Max Consecutive Sum                                    
 #  *                                                                    
 #  *  Prompt: Given an array of integers find the sum of consecutive    
 #  *          values in the array that produces the maximum value.      
 #  *                                                                    
 #  *  Input:  Unsorted array of positive and negative integers          
 #  *  Output: Integer (max consecutive sum)                            
 #  *                                                                    
 #  *  Time Complexity: O(n)                                             
 #  *  Auxiliary Space Complexity: O(1)                                  
 #  *                                                                    
 #  *  Example: input = [6, -1, 3, 5, -10]                               
 #  *           output = 13 (6 + -1 + 3 + 5 = 13)                        
 #  *                                                                    
 #  ****************************************************/
def maxConsecutiveSum(input):
	local_max = input[0]
	final_max = input[0]
	for i in range (1,len(input)):
		local_max = max(local_max+input[i],input[i])
		final_max = max(final_max,local_max)
	return final_max

#execution
options = raw_input("Do you want to enter custom values. Y/N? ")
if options == 'N':
	print "using default values as [6, -1 , 3 , 5 , -10]"
	print "result is", maxConsecutiveSum([6, -1 , 3 , 5 , -10])
else:
	print "Enter only numbers. To end press Enter twice."
	array = []
	c = raw_input("")
	while(len(c)>0):
		 array.append(int(c))
		 c= raw_input("")
	print "result is", maxConsecutiveSum(array)