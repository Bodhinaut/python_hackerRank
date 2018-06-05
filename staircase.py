def staircase(n):
	for value in range(1, n + 1):
		temp = value * ('#') 
		temp = temp.rjust(n)
		print(temp)

staircase(6)