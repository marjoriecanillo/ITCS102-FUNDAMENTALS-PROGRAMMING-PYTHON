colors = ['green', 'blue', 'yellow', 'red', 'orange', 'indigo']

#functions
colors.append('violet')
print(colors)
colors.pop()
print(colors)

for i in colors:
	print(f"{i}, color in the rainbow")

fullname = "Marjorie Canillo"

for v in fullname[-1: 0]:
	print(v)
print("\nReversed\n")
for n in fullname[::-1]:
	print(n)