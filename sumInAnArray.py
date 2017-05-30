# Problem: Given a sequence of nonnegative integers A and an integer T, return whether there is a *continuous sequence* of A that sums up to exactly T
# 
# Example:
# [23, 5, 4, 7, 2, 11], 20. Return True because 7 + 2 + 11 = 20
# [1, 3, 5, 23, 2], 8. Return True because 3 + 5 = 8
# [1, 3, 5, 23, 2], 7 Return False because no sequence in this array adds up to 7
# 

# Time complexity : O (N)  and NOT O(n^2)

#applying the idea of a floating sum
#we track the first element we are starting the sum at
#we keep adding elements to the sum till the sum either equals T or is greater than T
#if equal return True and it's done
#if greater, keep removing the first element contributing to the sum and increasing the index of that element (this is for refering to that value)

def sum_finder(A,T):

	floating_sum = 0
	first_val_in_sum = A[0]
	index_tracker = 0
	for value in xrange(0,len(A)):
		if floating_sum == T:
			print "Found"
			return True
		else:
			floating_sum += A[value]
			if floating_sum > T:
				while floating_sum > T :
					floating_sum -= first_val_in_sum
					index_tracker += 1
					first_val_in_sum = A[index_tracker]					
	if floating_sum == T:
		print "Found"
		return True
	else:
		print "Not Found"
		return False
			
			
sum_finder([23, 5, 4, 7, 2, 11], 20) #returns True
sum_finder([1, 3, 5, 23, 2], 8) #returns True
sum_finder([1, 3, 5, 23, 2], 7) # returns False

 




