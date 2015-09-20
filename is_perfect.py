'''
完美數(Perfect Number)指的是一個數子，
等於扣除自身以外所有正因數的加總，
寫函式判斷輸入的正整數是否為完美數。
2015/9/20(日) Mai 於 Esther 家中完成
'''

def is_perfect(x):
	sum = 0
	for i in range(1,x):
		if x % i == 0:
			sum = sum + i
	print bool(x == sum)
	
is_perfect(32)
