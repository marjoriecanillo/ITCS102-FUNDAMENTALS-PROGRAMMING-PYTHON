me = input("Hello! What is your name --> ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++")
print("ODD number compiler, type '0' to terminate the loop")

sum = 0
odd = ""
con = True

while con == True:
	you = eval(input("Please input a number --> "))

	if you % 2 == 1:
	 print("ODD number detected")
	 odd += str(you) + ","
	 sum += you
	 continue
	elif you == 0:
	 print("Loop Terminated")
	 break
	else:
	 if you % 2 == 0:
	  print("EVEN number, skipping... ")
	 else:
	  print("invalid number ")
	 continue

print(f"Hello {me}, The sum of all ODD number is {sum}")
print(f"All the ODD numbers you input is {odd}")