from activity25_1 import *
print("compiler")

choice = True
while choice == True:
    choose = input("Which activity do you want to run? \na - activity1\nb - activity2\nc - code_challenge1\nd - code_challenge2\ne - exit\nanswer: ")

    if choose == 'e':
        print("Exiting the program. Goodbye!")
        break
    elif choose == 'a':
        activity1()
    elif choose == 'b': 
        activity2()
    elif choose == 'c':
        code_challenge1()
    elif choose == 'd':
        code_challenge2()