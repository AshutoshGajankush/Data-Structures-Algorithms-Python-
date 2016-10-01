def sequential(alist, item):
	pos =0 
	found = False

	while pos<len(alist) and found == False:
		if(alist[pos]==item):
			found=True
		else:
			pos = pos+1
	return found

testlist = [1,2,3,4,5,6,7,8,9,]

print(sequential(testlist, 9))
print(sequential(testlist, 10))