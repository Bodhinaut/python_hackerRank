
def plusMinus(arr):
	constant = len(arr)
	pos_num = 0
	zero = 0
	neg_num = 0

	for value in arr:
		if value > 0:
			pos_num += 1
		elif value == 0:
			zero += 1
		elif value < 0:
			neg_num += 1
	print(str(pos_num) + ' ' + str(zero) + ' ' + str(neg_num) )
	pos_num /= constant
	neg_num /= constant
	zero /= constant

	print('%.6f' % round(pos_num, 6) )
	print('%.6f' % round(neg_num, 6) )
	print('%.6f' % round(zero, 6) )
	

plusMinus([-4, 3, -9, 0, 4, 1])