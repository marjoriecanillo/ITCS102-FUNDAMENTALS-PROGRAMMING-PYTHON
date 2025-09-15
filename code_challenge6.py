num = eval(input("Input a number --> "))

result = 1
for y in range(num, 0, -1):
	result *= y

print("Factorial is ",result)