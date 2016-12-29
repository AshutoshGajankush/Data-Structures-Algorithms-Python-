"""
Stacks as Lists. 
An implementation of opening and closing round braces checker, in string

"""
def parChecker(string):
	alist = []
	balanced = True
	for i in range(len(string)):
		if(string[i] == "("):
			alist.append(string[i])
		else:
			if(len(string) == 0):
				balanced = False
			else:
				alist.pop()
	if(balanced and len(alist) == 0):
		return True
	else:
		return False

print parChecker('((()))')
print parChecker('((()')

