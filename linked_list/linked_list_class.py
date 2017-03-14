import unittest

class Node(object):
	def __init__(self,value):
		self.data = value
		self.nextNode = None

class LinkedList(object):
	def __init(self,headNode = None):
		self.head = headNode
	def append(self,value):
		if self.head == None:
			self.head = Node(value)
		current = self.head
		while current.nextNode != None:
			current = current.nextNode
		current.nextNode = Node(value)
	def prepend(self,value):
		tmp = self.head
		self.head = Node(value)
		self.head.nextNode = tmp
	def delectWithValue(self,value):
		if self.head == None:
			print 'list is empty'
			return
		if self.head.data == value:
			self.head = self.head.nextNode
			return
		current = self.head
		hasValue = 0
		while current.nextNode != None:
			if current.nextNode.data == value:
				current.nextNode = current.\
							nextNode.nextNode
				hasValue = 1
				break
		if hasValue == 0:
			print 'list does not contain value '\
					+str(value)
			return 
	def print(self):
		if head == None:
			print 'list is empty'
			return 
		current = self.head
		while current.
class testLinkedList(unittest.TestCase):
	def test_construct(self):
		n1 = Node(1)
		n2 = Node(2)
		n3 = Node(3)
		n1.nextNode = n2
		n2.nextNode = n3
		ll = LinkedList(n1)
		
