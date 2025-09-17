print("MULTIPLICATION TABLE MAKER")
number = int(input("Enter a number: "))

for y in range(1, 11):
	mul = number * y
	print(number, "x", y, "=", mul)