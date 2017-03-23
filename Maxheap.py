class max_heap:
	def __init__(self, items =[]):
		"""
		Constructor

		Args: 
			items: a list of items to intialize heap with
		Return:
			 None
		"""

		self.heap = [0]
		for i in items:
			self.push(i)

	def push(self,data):
		"""
		Public function, used to push data into the max_heap

		Args:
			data: the data that needs to be pushed in.
		Returns:
			None	
		"""

		self.heap.append(data)
		self.__floatUp(len(self.heap)-1)

	def peek(self):
		"""
		Public function, used to get the node in the peak value

		Args:
			None
		Returns:
			max value / False
		"""

		if self.heap[1]:
			return self.heap[1]
		else:
			return False
	def pop(self):
		"""
		Public function, used to pop the max value in heap

		Args:
			None
		Returns:
			the max value / False
		"""

		if len(self.heap) > 2:
			self.__swap(1, len(self.heap)-1) 
			max = self.heap.pop()
			self.__bubbleDown(1)
		elif len(self.heap) == 2 :
			max = self.heap.pop()
		else:
			max = False
		return max

	def __swap(self, i, j):
		"""
		Private function that swaps to elements in the heap

		Args:
			i, j: index of elements needed to be swapped
		Returns:
			None
		"""

		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def __floatUp(self, index):
		"""
		Private function used to float up a value to it's right position,
		that satisifies the the child-parent relationship 
		after a push has been performed

		Args:
			index of value that needs to be floated up
		Returns:
			None
		"""

		parent = index//2
		if index <= 1:
			return
		elif self.heap[index] > self.heap[parent]:
			self.__swap(index, parent)
			self.__floatUp(parent)

	def __bubbleDown(self, index):
		"""
		Private function used to bubble down a value to it's right position,
		that satisifies the the child-parent relationship 
		after a pop   has been performed

		Args:
			index of value that needs to be floated up
		Returns:
			None
		"""

		left = index * 2
		right = index * 2 + 1
		largest = index
		if len(self.heap) > left and self.heap[largest] < self.heap[left]:
			largest = left
		if len(self.heap) > right and self.heap[largest] < self.heap[right]:
			largest = right
		if largest != index :
			self.__swap(index,largest)
			self.__bubbleDown(largest)

def merge_k_sorted_arrays(k, is_ascending):
	"""
	Merges K sorted arrays:
	Args:
		k : 2D array
		is_ascending : Boolean flag
	Returns:
		result: 1D array
	"""

	result= []
	for lists in k:
		for i in lists:
			m.push(i)
	for lists in k:
		for i in k:
			result.append(m.pop())	
	if is_ascending :
		result = result[::-1]
	return result


if __name__ == "__main__" :
	"""
	merging k sorted arrays
	"""
	
	m = max_heap([])
	k = [[1,3,5,7],
		[2,4,6],
		[8,9,10]]
	print merge_k_sorted_arrays(k,True)
