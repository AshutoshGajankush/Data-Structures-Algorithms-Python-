class Stacks:
	def __init__(self):
		self.items = []

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def is_empty(self):
		return self.items == [] # This line will return true if the condition is satisfied.

	def toString(self):
		print self.items

	
s =Stacks()
s.push('A')
s.push('B')
s.push(1)
s.toString()


while not s.is_empty():
	print s.pop(),

#IMPLEMENTATOON OF POSTFIX USING STACKS

import re
print re.split("([^0-9])", "123+456*/") 
# re.split allows us to specify regular expressions instead of delimiters
"""
Expressions: 
[A-z] :- the set of all letters
[0-9] :- the set of all numbers
^ :- negates a set e.g [^0-9] is the set of everything that is not number
"""

# EVALUATING POSTFIX USING STACKS

def eval_postfix(expr):
	import re
	token_list = re.split("([^0-9])", expr)
	stack = Stacks()
	for token in token_list:
		if token == '' or token == " ":
			continue
		if token == "+":
			sum = stack.pop() + stack.pop()
			stack.push(sum)
		elif token == '*':
			product = stack.pop() * stack.pop()
			stack.push(product)
		else:
			print token
			stack.push(int(token))
	return stack.pop()

print eval_postfix("56 47 + 2 *")

