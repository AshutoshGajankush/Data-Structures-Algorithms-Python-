# n is the size of the array
# m is the nummber of zeroes can be flipped
def findZeroes(arr, n, m):
	wL = 0			# Window left index
	wR = 0			# Window Right index
	bestL = 0		# Left index of widest window
	bestWindow = 0		
	zeroCount = 0	# Zero count which should be always less than m

	while (wR < n):
		"""
		Iterate from right till you reach the end and keep incrementing wR.
		And keep on increasing the window width.
		"""
		if(zeroCount <= m):
			if (arr[wR] == 0):
				zeroCount = zeroCount + 1
			wR = wR + 1

		"""
		Check if the no of zeroes in the window does not exceed m.
		If it does then start to decrese the size of window from the left.
		"""
		if (zeroCount > m):
			if (arr[wL] == 0):
				zeroCount = zeroCount - 1
			wL = wL + 1

		"""
		Keep on check the widest window for every iteration
		"""
		if(wR-wL > bestWindow):
			bestWindow = wR-wL
			bestL = wL;

	for i in range(bestWindow):
		if(arr[bestL + i] == 0):
			print (bestL + i),


arr = [1,0,0,1,1,0,1,0,1,1]
m = 2
n = len(arr)
print "Indexes of zeroes to be flipped are: ", findZeroes(arr, n, m)