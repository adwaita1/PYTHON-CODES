import queue
'''class for node of binary tree'''
class Node(object):
	"""docstring for Node"""
	def __init__(self, val=None):
		super(Node, self).__init__()
		self.left = None
		self.right = None
		self.val = val
		
'''class for binary tree'''
class BinaryTree(object):
	"""docstring for BinaryTree"""
	def __init__(self):
		super(BinaryTree, self).__init__()
		self.root = None

	'''Insert node level wise'''
	def insert(self, val):

		new_node = Node(val)
		if self.root is None:
			self.root = new_node
			return

		Q = queue.Queue(maxsize=20)
		Q.put(self.root)	#Enqueue
		while(Q.empty() is not True):
			temp = Q.get()	#Dequeue
			if temp.left:
				Q.put(temp.left)
			else:
				temp.left = new_node
				Q.queue.clear()
				return

			if temp.right:
				Q.put(temp.right)
			else:
				temp.right = new_node
				Q.queue.clear()
				return
		Q.queue.clear()

	'''Size of binary tree'''
	def size(self, root):
		if root is None:
			return 0
		return self.size(root.left) + 1 + self.size(root.right)

if __name__ == '__main__':
	btree = BinaryTree()

	btree.root = Node(1)
	btree.root.left =Node(2)
	btree.root.right = Node(3)
	btree.insert(4)
	btree.insert(5)
	btree.insert(6)
	print(btree.size(btree.root))