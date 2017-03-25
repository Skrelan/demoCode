tracker = 0
class Node:
	def __init__(self,data):
		self.left_child = None
		self.right_child = None
		self.value = data
		
	def insert(self,data):
		if self.value == data: #Assuming the Tree has unique elements only
			return False
		elif self.value > data:
			if self.left_child:
				self.left_child.insert(data)
			else:
				self.left_child = Node(data)
		else:
			if self.right_child:
				self.right_child.insert(data)
			else:
				self.right_child = Node(data)

		
				
class BinaryTree:
	def __init__(self):
		self.root = None
		self.size = 0
		
	def insert(self,data):
		if self.size == 0:
			self.size = self.size + 1
			self.root = Node(data)
		else:
			self.size = self.size + 1
			self.root.insert(data)
	
	def breath_first_search(self): #Works
		Quee = [self.root.value]
		tracker = [self.size]
		def helper(node):
			if tracker[0] <= 0:
				return
			else:
				if node.left_child:
					Quee.append(node.left_child.value)
					tracker[0] = tracker[0] - 1
				if node.right_child:
					Quee.append(node.right_child.value)
					tracker[0] = tracker[0] - 1
				if node.left_child:	
					helper(node.left_child)
				if node.right_child:
					helper(node.right_child)
		helper(self.root)
		print Quee
		
	def DFS(self):
		result = []
		def traverse(node):
			if node == None:
				return
			else:
				result.append(node.value) #V
				traverse(node.left_child)	#L
				traverse(node.right_child)	#R
		traverse(self.root)
		print result
			
		
a = BinaryTree()
#4, 2, 5, 1, 3, 7, 6, 8
a.insert(4)
a.insert(2)
a.insert(5)
a.insert(1)	
a.insert(3)
a.insert(7)
a.insert(6)
a.insert(8)
		
a.breath_first_search()
a.DFS()