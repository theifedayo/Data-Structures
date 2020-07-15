"""Class of Node and Linkedlist created with different methods for the 
LinkedList class"""

#Node object created with data and next-pointer attributes
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

#Linkedlist object created with the head attributes[the first node in a link]
class LinkedList:
	
	def __init__(self):
		self.head = None
		
	def print_list(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.data)
			cur_node = cur_node.next
	
	#Add data to the end of your linkedlist
	def append(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node
	
	#Add  data to the beginning of your linkedlist
	def prepend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
		
	def insert(self, prev_node, data):
		if prev_node is None:
			print("There is no previous node as such")
			return
		new_node = Node(data)
		new_node.next = prev_node.next
		prev_node.next = new_node
		
		
		
	#This method deletes val from your linkedlist
	def delete(self, val):
		cur_node = self.head
		if cur_node.data == val:
			cur_node = cur_node.next
			cur_node = None
			return
		
		prev = None
		while cur_node and cur_node.data != val:
			prev = cur_node
			cur_node = cur_node.next
		
		if cur_node is None:
			return
		prev.next = cur_node.next
		cur_node = None
		
	#This method deletes val at a specified positon from your linkedlist
	def delete_pos(self, pos):
		cur_node = self.head
		if pos == 0:
			self.head = cur_node.next
			cur_node = None
			return
		prv = None
		count = 1
		while cur_node and count != pos:
			prev = cur_node
			cur_node = cur_node.next
			count += 1
			
		if cur_node is None:
			return
		prev.next = cur_node.next
		cur_node = None

	#This method returns the number of node in the linkedlist
	def list_len(self):
		count = 0
		cur_node = self.head
		while cur_node:
			count += 1
			cur_node = cur_node.next
		return count


		
#Applications
linked = LinkedList()
linked.append("A")
linked.append("B")
linked.append("D")
linked.append("E")
linked.append("F")
linked.delete_pos(4)


linked.insert(linked.head.next,"C")
print(linked.list_len())

linked.print_list()
			
		
		
			
		
		
		
