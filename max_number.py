'''
讀檔案後列出檔案中最大的 3 組數字
2015/9/20(日) Mai 於 Esther 家中完成
'''

with open("number.txt") as f:
	number = []
	for num in f:
		number.append(num)

bigone = 0
bigtwo = 0
bigthree = 0
for i in number:
	if i > bigone:
		bigone = i
print bigone
for j in number:
	if j > bigtwo:
		if j != bigone:
			bigtwo = j
print bigtwo
for k in number:
	if k > bigthree:
		if k != bigone and k != bigtwo:
			bigthree = k
print bigthree	
	
