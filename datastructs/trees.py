# /*********************************************************************************** 
#   *                                                                                *
#   *                                                                                *
#   *  Problem: Binary Search Tree                                                   *
#   *                                                                                *
#   *  Prompt: Create a BinarySearchTree class/constructor.                          *
#   *          Name it binarySearchTree (js) or binary_search_tree (rb/py).          *
#   *                                                                                *
#   *          Part 1: Create a node class for your binarySearchTree.                *
#   *                  Your node class will take an integer value and output         *
#   *                  an object with the following properties:                      *
#   *                                                                                *
#   *                  node.value: input value                                       *
#   *                  node.leftChild: a pointer to the left child Node              * 
#   *                  node.rightChild: a pointer to the right child Node            *
#   *                                                                                *
#   *                  Example: { value: 1, leftChild: null, rightChild: null }      *
#   *                                                                                *
#   *          Part 2: Create the BinarySearchTree class.                            *
#   *                  It should contain the following properties:                   *
#   *                                                                                *
#   *                  root: pointer to the root node                                *
#   *                  size: number of nodes in the BinarySearchTree                 *
#   *                                                                                *
#   *                  The BinarySearchTree will also have the following properties: *
#   *                                                                                *
#   *                  insert: method that takes takes an input value, and creates a *
#   *                          new node with the given input.  The method will then  *
#   *                          find the correct place to add the new node. (Remember *
#   *                          that nodes with values larger than the parent node go *
#   *                          to the right, and smaller values go to the left.)     *
#   *                                                                                *
#   *                  search: method that will search to see if a node with a       *
#   *                          specified value exists.  If present returns true,     *
#   *                          else returns false.                                   *
#   *                                                                                *
#   *  Input:  N/A                                                                   *
#   *  Output: A BinarySearchTree instance                                           *
#   *                                                                                *
#   *  What are the time and auxilliary space complexities of the various methods?   *
#   *                                                                                *
#   **********************************************************************************/


#  /**
#   *  Extra Credit: Remove
#   *
#   *  Prompt: Create a remove method on your BinarySearchTree that will remove and
#   *          return a given value from the tree and retie the tree so it remains
#   *          properly sorted.
#   **/

class Node:
	def __init__(self, data):
		self.value = data
		self.left = None
		self.right = None
	
	def insert(self, data):
		print"im in"
		if self.value == data:
			return False
		elif self.value>data:
			if self.left:
				print "left"
				return self.left.insert(data) #recurision
			else:
				self.left = Node(data)
				return True
		else:
			if self.right:
				print" right"
				return self.right.insert(data)
			else:
				self.right = Node(data)
				return True
				
			
class Binary_Search_Tree:
	def __init__(self): 
		self.root = None
		self.size = 0
		
	def insert(self, val):
		node = Node(val)
		if self.root:
			print "going on a trip"
			return self.root.insert(val)
		else:
			self.root = node
			return True
	
  # def insert(self, val):
	# node = Node(val)
	# def helper(tracker):
		# a = 1 
		# if a == 1:#((not tracker.right == None) | (not tracker.left == None)):
			# if (node.value > tracker) & (not tracker.right == None):
				# print "tracker at node value",tracker.value
				# tracker = tracker.right
				# helper(tracker)
			# elif (node.value < tracker) & (not tracker.left == None):
				# print "tracker at node value",tracker.value
				# tracker = tracker.left	
				# helper(tracker)
		# else:
			# return tracker
	# if self.size == 0:
		# self.root = node
		# self.size = self.size + 1
	# else:
		# root = self.root
		# tracker = helper(root)
		# if node.value > tracker:
			# tracker.right = node.
			
		# else:
			# tracker.left = node
		# self.size += 1	
		
	def search(self, searchVal):
		root = self.root
		def helper(tracker,value):
			if tracker.value == value:
				print "value has been found"
			elif (value < tracker.value) & (not tracker.left == None) :
				tracker = tracker.left
				helper(tracker,value)
			elif (value > tracker.value) & (not tracker.right == None):
				tracker = tracker.right
				helper(tracker,value)
			else:
				print "value not found !"
		helper(root,searchVal)
#   def remove(self, removeval=None):
#	def prints(self):
#		root = self.root
#		def helper(tracker):
#			print tracker.value
    
BT = Binary_Search_Tree()
for i in range(0,5):
	BT.insert(int(raw_input("")))
for i in range(0,5):
	BT.search(int(raw_input("")))



