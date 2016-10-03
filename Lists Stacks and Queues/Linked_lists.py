class Node:
	def __init__(self,cargo = None, next=None):
		self.cargo = cargo
		self.next = next

	def __str__(self):
		return str(self.cargo)

# Three nodes of Linked lists are generated.
node1= Node(1)
node2 = Node(2)
node3 = Node(3)
# node1 and node 2 are assigned pointers to the next node
node1.next = node2
node2.next = node3

def print_list(node):
	while node:
		print node
		node = node.next


def print_backwards(list):
	if list==None:
		print "Got u"
		return
	print_backwards(list.next)
	print list
print_backwards(node1)

# Removing the second node from the list
def remove_second(list):
	first = list
	second = list.next # save the item to be removed fro returning
	first.next = second.next # Make frist node to point to third node
	second.next = None
	return second

remove = remove_second(node1)
print "Removed node is: ", remove

print_list(node1)