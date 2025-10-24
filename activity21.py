ems = True

while ems == True:
	ans = input("Do you wish to stop washing (yes/no)--> ")

	if ans == "no":
	 print("continue the cycle")
	 continue
	elif ans == "yes":
	 print("cycle stops")
	 break
	else:
	 print("invalid choice")
	