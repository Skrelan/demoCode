"""
Trees are fun

Traversal in graphs happen in two ways,
Breadth First Search : Use Queue
Depth First Search : Use Stacks : Preorder, Inorder, Postorder
"""

#Node : value + pointrer(s)
class Node:
    def __init__(self,data=0):
        self.value = data
        self.left = None
        self.right = None

    def insert(self,data): #This must be done in Node because, if we don't do this, it is NOT possible to store children nodes, because of the self thingy
        if self.left == None :
            self.left = Node(data)
            return True
        if self.right == None :
            self.right = Node(data)
            return True
        return False

class Trees:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self,data):
        queue = []
        if self.root == None:
            self.root = Node(data)
            return
        queue.append(self.root)
        while True:
            print [x.value for x in queue]
            if len(queue) == 0:
                return
            curr = queue[0]
            if curr.insert(data) == False:
                queue.append(curr.left)
                queue.append(curr.right)
                queue = queue[1:]
            else:
                return
        print "End"

    def bfs_traversal(self):
        queue = []
        result = []
        if self.root == None:
            return None, "Empty Tree"
        queue = [self.root]
        while True:
            if len(queue) == 0:
                return result, None
            curr = queue[0]
            result.append(curr.value)
            print curr.value
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            queue = queue[1:]

    def dfs_preorder(self): #VLR #using a STACK, complicated
        stack = []
        result = []
        if self.root == None:
            return None, "Empty Tree"
        stack.append(self.root)
        def helper():
            if len(stack) == 0:
                print result
                return result, None
            curr = stack.pop()
            result.append(curr.value)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            helper()
        return helper()

    def dfs_pre_order(self): #VLR
        result = []
        if self.root == None:
            return None, "Empty Tree"
        def helper(node):
           if node is not None:
              result.append(node.value)
              helper(node.left)
              helper(node.right)
        helper(self.root)
        return result, None

    def dfs_in_order(self): #LVR
        result = []
        if self.root == None:
            return None, "Empty Tree"
        def helper(node):
           if node is not None:
              helper(node.left)
              result.append(node.value)
              helper(node.right)
        helper(self.root)
        return result, None

    def dfs_post_order(self): #VRL
        result = []
        if self.root == None:
            return None, "Empty Tree"
        def helper(node):
           if node is not None:
              helper(node.left)
              helper(node.right)
              result.append(node.value)
        helper(self.root)
        return result, None

    def dfs_pre_order_search(self,data): #VLR
        result = False
        if self.root == None:
            return False, "Empty Tree"
        def helper(node):
           if node is not None:
              if data = node.value:
                  return True, None
              helper(node.left)
              helper(node.right)
        helper(self.root)
        return result, None

    def dfs_in_order_search(self,data): #LVR
        result = False
        if self.root == None:
            return None, "Empty Tree"
        def helper(node):
           if node is not None:
              helper(node.left)
              if node.value == data:
                  return True, None
              helper(node.right)
        helper(self.root)
        return result, None

    def dfs_post_order_search(self,data): #VRL
        result = None
        if self.root == None:
            return None, "Empty Tree"
        def helper(node):
           if node is not None:
              helper(node.left)
              helper(node.right)
              if node.value == data:
                  return True, None
        helper(self.root)
        return result, None

tree = Trees()
def tests():
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    print tree.bfs_traversal()
    print tree.dfs_pre_order()
    print tree.dfs_in_order()
    print tree.dfs_post_order()
    print dfs_pre_order_search(5)
    print dfs_pre_order_search(7)
