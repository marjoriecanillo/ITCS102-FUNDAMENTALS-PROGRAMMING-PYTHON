print("\t\t   *")
for s in range(1,11,1):
    for z in range(10,s,-1):
        print(" ", end=" ")
    for r in range(0,s,1):
        print("*", end=' ')
    for n in range(0,s,1):
        print("*", end=" ")
    print()
for m in range(1,10,1):
    for h in range(0,m,1):
        print(" ", end=" ")
    for b in range(10,m,-1):
        print("*", end=' ')
    for w in range(10,m,-1):
        print("*", end=' ')
    print()
print("\t\t   *")