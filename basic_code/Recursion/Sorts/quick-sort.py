#Step1: We select a Piviot point
#Step2: put all elements smaller than the piviot point to its left, and let the larger elements stay on the right
#Step3: Recursively call it self on smaller and larger subsection
#Step4: When we are done we should have a sorted array
import math
def QuickSort(array):
	print "Function called",array
	if (len(array) <= 1):
		return array
	else:	
		index =  int(math.floor(len(array)/2))
		piviot = [array[index]]
		smaller = []
		bigger = []
		for val in range(0,len(array)):
			if  (array[val]<piviot[0]):
				smaller.append(array[val])
				continue
			if (array[val]>piviot[0]):
				bigger.append(array[val])
				continue
		print ">>>>S",smaller,"B",bigger,"P",piviot,"a",array
		smaller = QuickSort(smaller)
		bigger = QuickSort(bigger)
		smaller.extend(piviot)
		smaller.extend(bigger)
		return smaller
	

arr =map(int, (raw_input("Enter Array of numbers seperated by single spaces: ").split(" ")))
print "Before Sort",arr,"\n"
arr = QuickSort(arr)
print "After Sort",arr				
			