# -*- coding: utf8 -*-

for i in range(1,10):
	if i == 1: 
			msg = '一'
	if i == 2:
			msg = '二'
	if i == 3:
			msg = '三'
	if i == 4:
			msg = '四'
	if i == 5:
			msg = '五'
	if i == 6:
			msg = '六'
	if i == 7:
			msg = '七'
	if i == 8:
			msg = '八'
	if i == 9:
			msg = '九'		

	for j in range(1,10):
		if j == 1: 
			msg2 = '一'
		if j == 2:
			msg2 = '二'
		if j == 3:
			msg2 = '三'
		if j == 4:
			msg2 = '四'
		if j == 5:
			msg2 = '五'
		if j == 6:
			msg2 = '六'
		if j == 7:
			msg2 = '七'	
		if j == 8:
			msg2 = '八'
		if j == 9:
			msg2 = '九'

		k = i*j
		string = str(k)
		if len(string) == 1:
			if k == 1:
				msg3 = '一'
			if k == 2:
				msg3 = '二'
			if k == 3:
				msg3 = '三'
			if k == 4:
				msg3 = '四'
			if k == 5:
				msg3 = '五'
			if k == 6:
				msg3 = '六'
			if k == 7:
				msg3 = '七'	
			if k == 8:
				msg3 = '八'
			if k == 9:
				msg3 = '九'
		if len(string) == 2:
			left = int(string[:1])
			right = int(string[-1:])
			if left == 1:
				left1 = '一'
			if left == 2:
				left1 = '二'
			if left == 3:
				left1 = '三'
			if left == 4:
				left1 = '四'
			if left == 5:
				left1 = '五'
			if left == 6:
				left1 = '六'
			if left == 7:
				left1 = '七'	
			if left == 8:
				left1 = '八'
			if left == 9:
				left1 = '九'

			if right == 1:
				right1 = '一'
			if right == 2:
				right1 = '二'
			if right == 3:
				right1 = '三'
			if right == 4:
				right1 = '四'
			if right == 5:
				right1 = '五'
			if right == 6:
				right1 = '六'
			if right == 7:
				right1 = '七'	
			if right == 8:
				right1 = '八'
			if right == 9:
				right1 = '九'
			if right == 0:
				right1 = '零'
			msg3 = left1 + right1 
		print msg,'乘',msg2,'等於', msg3
