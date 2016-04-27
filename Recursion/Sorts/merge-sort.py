def  MergeSort(array):
		Result = array
		if len(array)>1:
			mid = len(array)//2
			left = array[:mid]
			right = array[mid:]
			print "arr is",array
			MergeSort(left)
			#print "Left is done",left
			MergeSort(right)
			#print "Right is done",right
			i = 0
			j = 0
			k = 0
			while (i < len(left) )& (j <len(right)):
				if left[i] < right[j]:
					array[k] = left[i]
					i = i + 1
				else:
					array[k] = right[j]
					j = j + 1
				k = k + 1
			while i < len(left):
					array[k]=left[i]
					i = i + 1
					k = k + 1
			while j < len(right):
					array[k]=right[j]
					j = j+ 1
					k = k + 1
		
			
		#print Result

arr = map(int,(raw_input("Enter Array of numbers seperated by single spaces: ").split(" ")))
print "Before Sort",arr
MergeSort(arr)
print "After Sort",arr	


#Advantages  of Merge Sort
#1. O(n log n) time Complexity
#2. Stable sort	

#Disadvantages
#1. Duplicate array , Auxilary space O(n))
#2. Worst case is also O(n Log n) time
#3. A lil slow