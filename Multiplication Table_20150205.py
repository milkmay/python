# -*- coding: utf8 -*-

list = ["拾","一","二","三","四","五","六","七","八","九"]

for i in range(1,10):
	msg1 = list[i]
 	for j in range(1,10):
 		msg2 = list[j]
 		k = i * j
 		string = str(k)
 		if len(string) == 1:
 			msg3 = list[k]
 		if len(string) == 2:
 			left = int(string[:1])
			right = int(string[-1:])
			if right == 0:
				msg3 = list[left]+list[right]
 			else:
 				msg3 = list[left]+dic[0]+list[right]
		print msg1,'乘',msg2,'等於', msg3
