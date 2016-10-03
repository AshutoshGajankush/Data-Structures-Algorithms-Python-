# Hashtable implementation, Order is O(1)
def hashTable(d1, x, y, z):
	print "Searched Item:",search(d1,x)
	print "Deleted Item:",delete(d1,y)
	"Added element is: ", add(d1,z)


def search(d, y):
	cal = y%5 #hashfunction
	return d[cal]

def delete(d,z):
	cal = z%5
	return d.pop(cal)

def add(d,z):
	cal = z%5
	d[cal] = z
 # 5 is considered as the length of the hashtable
a = {1:1,2:7,4:4,0:5}
print a
hashTable(a , 7, 4,3)
print a