temp =eval(input("Enter temperature --> "))
if temp <= 0:
	print("Temperature outside is freezing cold")
elif temp >= 1 and temp <= 20:
	print("Temperature outside is cold")
elif temp >= 21 and temp <= 30:
	print("Temperature outside is lukewarm")
elif temp >= 31 and temp <= 40:
	print("Temperature outside is warm")
elif temp >= 41 and temp <= 50:
	print("Temperature outside is hot")
elif temp >= 51 and temp <= 60:
	print("Temperature outside is boiling hot")
else:
	print("Invalid temperature")