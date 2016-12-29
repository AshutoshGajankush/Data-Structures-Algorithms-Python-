"""
Stacks as Lists. 
An implementation of opening and closing round braces checker, in string

"""

def parChecker(string):
	alist = []
	balanced = True
	for i in range(len(string)):
		if(string[i] in "([{"):
			alist.append(string[i])
		else:
			if(len(string) == 0):
				balanced = False
			else:
				value = alist.pop()
				if not matches(value, string[i]):
					balanced = False

	if(balanced and len(alist) == 0):
		return True
	else:
		return False

def matches(open, close):
	opens = "([{"
	closers = ")]}"
	return opens.index(open) == closers.index(close)

print parChecker('{{([][])}()}')
print parChecker('([)]')

