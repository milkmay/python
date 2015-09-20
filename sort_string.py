
mylist = ["CDEF","ABC","FIJK"]
mylist.sort()
listlen = len(mylist)

'''
print mylist[0]
print mylist[1]
print mylist[2]
print listlen
'''

dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, 
"F": 6, "G": 7, "H": 8, "I": 9, "J": 10, 
"K": 11, "L": 12, "M": 13, "N": 14, "O": 15, 
"P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, 
"U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

totalsum = 0
for lilen in range(listlen):
	sum = 0
	tmpsum = 0
	tmpstr = mylist[lilen]
	strlen = len(tmpstr)
	#print tmpstr
	#print strlen
	for strlen in range(len(tmpstr)):
		tmpsum = tmpsum + dict[tmpstr[strlen]]
		sum = tmpsum * (lilen+1)
	#print tmpsum
	totalsum = totalsum + sum
print totalsum
