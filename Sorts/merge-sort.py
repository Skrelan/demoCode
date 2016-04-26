def  MergeSort(arr):
		stack = []
		def Split(array):
			
			left = [:(len(array)/2)]
			right = [(len(array)/2):]
			