num = 0
for y in range(1, 11, 1):
	number = eval(input("Input number: "))
	if number % 2:
	 num += number
print("The sum of all the ODD number is ",num)