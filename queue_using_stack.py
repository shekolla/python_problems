'''
	Implementing a Queue using a stack
	Queue:
		First Come First Serve
	Stack:
		Last Come First Serve
'''

class Queue:
	def __init__(self):
		self.li1 = []
		self.li2 = []

	# To add an element to the end
	def enqueue(self, element):
		self.li1.append(element)
	
	# To remove element from the front 
	def dequeue(self):
		while (len(self.li1)):
			self.li2.append(self.li1.pop())
		self.li2.pop()
		while (len(self.li2)):
			self.li1.append(self.li2.pop())

	# repr should always return a string
	def __repr__(self):
		return f'{self.li1}'