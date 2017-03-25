class max_heap:
	def __init__(self, data):
		self.heap = [0]
		for val in data:
			self.push(data)

	def push(self, data):
		self.heap.append(data)
		self.__foat_up(len(heap)-1)

	def pop(self):
		if len(self.heap) > 2:
			self.swap(1,len(heap)-1)
			value = self.heap.pop()
			self.__bubble_down(1)
		elif len(self.heap) == 2:
			self.heap.pop()
		else:
			return False

	def peek(self):
		if self.heap[1]:
			return self.heap[1]
		else:
			return False

	def __swap(self,i,j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def __float_up(self,index):
		parent = index//2
		if index <=1:
			return
		elif self.heap[index] > self.heap[parent]:
			self.__swap(index,parent)
			self.__float_up(parent)

	def __bubble_down(self, index):
		left_child = index * 2 
		right_child = index * 2 + 1
		largest = index
		if len(self.heap) > left and self.heap[largest] < self.heap[left]
			largest = left
		if len(self.heap) > right and self.heap[largest] < self.heap[right]
			largest = right
		if largest != index :
			self.__swap(index,largest)
			self.__bubble_down(largest)
