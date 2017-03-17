import unittest
import linked_list_class as ll

class testLinkedList(unittest.TestCase):
	def test_construct(self):
		n1 = ll.Node(1)
		n2 = ll.Node(2)
		n3 = ll.Node(3)
		n1.nextNode = n2
		n2.nextNode = n3
		llist = ll.LinkedList(n1)
		llist.printList()
	def test_delectWithValue(self):
		n1 = ll.Node(1)
		n2 = ll.Node(2)
		n3 = ll.Node(3)
		n1.nextNode = n2
		n2.nextNode = n3
		llist = ll.LinkedList(n1)
		llist.delectWithValue(4)
		llist.delectWithValue(3)
		llist.printList()
if __name__=='__main__':
	unittest.main()
