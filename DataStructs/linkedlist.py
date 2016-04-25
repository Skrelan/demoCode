# /********************************************************************************** 
#  *                                 Homework IV                                    *
#  *                                                                                *
#  *  Problem: Linked List                                                          *
#  *                                                                                *
#  *  Prompt: Create a Linked List class/constructor.                               *
#  *          Name it LinkedList (js) or Linked_List(rb/py).                        *
#  *                                                                                *
#  *          Part 1: Create a node class for your LinkedList.                      *
#  *                  Your node class will take an integer value and output         *
#  *                  and output and object with the following properties:          *
#  *                                                                                *
#  *                  node.value: input value                                       *
#  *                  node.next: a pointer to the next value (initiall null)        * 
#  *                                                                                *
#  *                  Example: { value: 1, next: null }                             *
#  *                                                                                *
#  *          Part 2: Create the LinkedList class.                                  *
#  *                  It should contain the following properties:                   *
#  *                                                                                *
#  *                  head: pointer to the head node                                *
#  *                  tail: pointer to the tail node                                *
#  *                  length: number of nodes in the linked list                    *
#  *                                                                                *
#  *                  The LinkedList should also contain the following properties   *
#  *                                                                                *
#  *                  append: function that adds a node to the tail                 *
#  *                                                                                *
#  *                  insert: function that takes in two values, one to be inserted *
#  *                          and one to search.  It searches the list for the      *
#  *                          search value, and if found, adds a new node with the  *
#  *                          insert value after the node with the search value.    *
#  *                                                                                *
#  *                  delete: function that removes a node at a specified location, *
#  *                          with a default action of deleting the head            *
#  *                                                                                *
#  *                  contains: function that checks to see if a value is contained *
#  *                            in the list                                         *
#  *                                                                                *
#  *  Input:  N/A                                                                   *
#  *  Output: A LinkedList instance                                                 *
#  *                                                                                *
#  *  What are the time and auxilliary space complexities of the various methods?   *
#  *                                                                                *
#  **********************************************************************************/

class Node: 
  def __init__(self, data = 0): 
    self.value = data
    self.next = None

class Linked_List:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
      
  def append(self, val):
		node = Node(val)
		if self.length == 0:
			self.head = node
			self.tail = node
			self.length = 1
		else:
			self.tail = node
			self.length= self.length+1
			node2 = self.head
			#for i in range (0,self.length):
			#	node2.value = node2.next
			#node2.next = node

  def insert(self, insertVal=None, searchVal=None):
		node = Node(insertVal)
		if self.length == 0:
			print "No elements in list"
			return
		node2 = self.node
		for i in range(0,self.length):
			if node.value == searchVal:
				node.next = node2.next
				node2.next = node
				return
			node2.value = node2.next
		print "Element with value",searchVal,"not found"
		return
		
  
  #def delete(self, loc=None): 
      
  #def contains(self, searchVal=None): 
	
  def travel(self):
	node = self.head
	for val in range (0,self.length):
		print node.value
		node = node.next

a = Linked_List()
c = ""
c = int(raw_input(""))
while(not c == -1):
		a.append(c)
		c = int(raw_input(""))
a.travel()
#raw_input("")
		
		
		


