for me in range(1,7,1):
	for us in range(7,me,-1):
	 print(" ", end=' ')
	for you in range(me,0,-1):
	 print(you, end=' ')
	for them in range(2,me+1):
	 print(them, end=' ')
	print()