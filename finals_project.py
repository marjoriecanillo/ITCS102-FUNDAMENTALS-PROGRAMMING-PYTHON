from def_function import *

print("Welcome to my Finals Project")

name = input("Hello, please input your name --> ")
print(f"Hi, {name}, Welcome to my Compiler Program")

isTrue = True

while isTrue == True:
    print("Pick a Choice: ")
    print("1 - Activities\n2 - Code_Challenges\n0 - Stop The Program")
    choice = input("Enter your choice: ")

#Activities
    if choice == "0":
        print("Stopping the program.")
        break

    elif choice == "1":
        print("Welcome to my Activities Program")
        print("Choose between the given letters: ")
        print("\nA - Activity (1-5)\nB - Activity (6-10)\nC - Activity (11-15)\nD - Activity (16-20)\nE - Activity (21-24_1)\nF - Activity (26-28)\nS - Stop")
        act = input("Choose a letter:  ").lower()
        if act == "a":
            print(f"You've selected letter {act}")
            print("Welcome to Activities 1 to 5")
            print("Choose between the given options: ")
            print("1a - Activity1\n2a - Activity2\n3a - Activity3\n4a - Activity4\n5a - Activity5")
            act01 = input("Choose the following options:  ").lower()
            if act01 == "1a":
                print(f"You've selected number {act01}")
                print("Welcome to my first python activity")
                activity1()
                continue
            elif act01 == "2a":
                print(f"You've selected number {act01}")
                print("Welcome to my second python activity")
                activity2()
                continue
            elif act01 == "3a":
                print(f"You've selected number {act01}")
                print("Welcome to my third python activity")
                activity3()
                continue
            elif act01 == "4a":
                print(f"You've selected number {act01}")
                print("Welcome to my fourth python activity")
                activity4()
                continue
            elif act01 == "5a":
                print(f"You've selected number {act01}")
                print("Welcome to my fifth python activity")
                activity5()
                continue
            else:
                print("Invalid input...please, try again")
                continue

        elif act == "b":
            print(f"You've selected letter {act}")
            print("Welcome to Activities 6 to 10")
            print("Choose between the given options: ")
            print("6a - Activity6\n7a - Activity7\n8a - Activity8\n9a - Activity9\n10a - Activity10")
            act01 = input("Choose the following options:  ").lower()
            if act01 == "6a":
                print(f"You've selected number {act01}")
                print("Welcome to my sixth python activity")
                activity6()
                continue
            elif act01 == "7a":
                print(f"You've selected number {act01}")
                print("Welcome to my seventh python activity")
                activity7()
                continue
            elif act01 == "8a":
                print(f"You've selected number {act01}")
                print("Welcome to my eighth python activity")
                activity8()
                continue
            elif act01 == "9a":
                print(f"You've selected number {act01}")
                print("Welcome to my ninth python activity")
                activity9()
                continue
            elif act01 == "10a":
                print(f"You've selected number {act01}")
                print("Welcome to my tenth python activity")
                activity10()
                continue
            else:
                print("Invalid input...please, try again")
                continue

        elif act == "c":
            print(f"You've selected letter {act}")
            print("Welcome to Activities 11 to 15")
            print("Choose between the given options: ")
            print("11a - Activity11\n12a - Activity12\n13a - Activity13\n14a - Activity14\n15a - Activity15")
            act01 = input("Choose the following options:  ").lower()
            if act01 == "11a":
                print(f"You've selected number {act01}")
                print("Welcome to my eleventh python activity")
                activity11()
                continue
            elif act01 == "12a":
                print(f"You've selected number {act01}")
                print("Welcome to my twelfth python activity")
                activity12()
                continue
            elif act01 == "13a":
                print(f"You've selected number {act01}")
                print("Welcome to my thirteenth python activity")
                activity13()
                continue
            elif act01 == "14a":
                print(f"You've selected number {act01}")
                print("Welcome to my fourteenth python activity")
                activity14()
                continue
            elif act01 == "15a":
                print(f"You've selected number {act01}")
                print("Welcome to my fifteenth python activity")
                activity15()
                continue
            else:
                print("Invalid input...please, try again")
                continue
            
        elif act == "d":
            print(f"You've selected letter {act}")
            print("Welcome to Activities 15 to 20")
            print("Choose between the given options: ")
            print("16a - Activity16\n17a - Activity17\n18a - Activity18\n19a - Activity19\n20a - Activity20")
            act01 = input("Choose the following options:  ").lower()
            if act01 == "16a":
                print(f"You've selected number {act01}")
                print("Welcome to my sixteenth python activity")
                activity16()
                continue
            elif act01 == "17a":
                print(f"You've selected number {act01}")
                print("Welcome to my seventeenth python activity")
                activity17()
                continue
            elif act01 == "18a":
                print(f"You've selected number {act01}")
                print("Welcome to my eighteenth python activity")
                activity18()
                continue
            elif act01 == "19a":
                print(f"You've selected number {act01}")
                print("Welcome to my nineteenth python activity")
                activity19()
                continue
            elif act01 == "20a":
                print(f"You've selected number {act01}")
                print("Welcome to my twentieth python activity")
                activity20()
                continue
            else:
                print("Invalid input...please, try again")
                continue
        
        elif act == "e":
            print(f"You've selected letter {act}")
            print("Welcome to Activities 21 to 24_1")
            print("Choose between the given options: ")
            print("21a - Activity21\n22a - Activity22\n23a - Activity23\n24a - Activity24\n24_1a - Activity24_1")
            act01 = input("Choose the following options:  ").lower()
            if act01 == "21a":
                print(f"You've selected number {act01}")
                print("Welcome to my twenty-first python activity")
                activity21()
                continue
            elif act01 == "22a":
                print(f"You've selected number {act01}")
                print("Welcome to my twenty-second python activity")
                activity22()
                continue
            elif act01 == "23a":
                print(f"You've selected number {act01}")
                print("Welcome to my twenty-third python activity")
                activity23()
                continue
            elif act01 == "24a":
                print(f"You've selected number {act01}")
                print("Welcome to my twenty-fourth python activity")
                activity24()
                continue
            elif act01 == "24_1a":
                print(f"You've selected number {act01}")
                print("Welcome to my twenty-f0urth underscore one python activity")
                activity25()
                continue
            else:
                print("Invalid input...please, try again")
                continue

        elif act == "f":
            print(f"You've selected letter {act}")
            print("Welcome to Activities 26 to 28")
            print("Choose between the given options: ")
            print("26a - Activity26\n27a - Activity27\n28a - Activity28")
            act01 = input("Choose the following options:  ").lower()
            if act01 == "26a":
                print(f"You've selected number {act01}")
                print("Welcome to my twenty-sixth python activity")
                activity26()
                continue
            elif act01 == "27a":
                print(f"You've selected number {act01}")
                print("Welcome to my twenty-seventh python activity")
                activity27()
                continue
            elif act01 == "28a":
                print(f"You've selected number {act01}")
                print("Welcome to my twenty-eighth python activity")
                activity28()
                continue
            else:
                print("Invalid input...please try again")
                continue

        elif act == "s": 
            print("Stopping The Program... ")
            break
        else:
            print("Invalid input, choose only between the given choices.")
            continue

#Code Challenges
    if choice == "2":
        print("Welcome to my Code Challenges Program")
        print("Choose between the given letters: ")
        print("\nA - Code_Challenge (1-5)\nB - Code_Challenge (6-10)\nC - Code_Challenge (11-15)\nD - Code_Challenge (16)\nS - Stop")
        act = input("Choose a letter:  ").lower()
        if act == "a":
            print(f"You've selected letter {act}")
            print("Welcome to Code_Challenges 1 to 5")
            print("Choose between the given options: ")
            print("1c - Code_Challenge1\n2c - Code_Challenge2\n3c - Code_Challenge3\n4c - Code_Challenge4\n5c - Code_Challenge5")
            act01 = input("Choose the following options:  ").lower()
            if act01 == "1c":
                print(f"You've selected number {act01}")
                print("Welcome to my first code challenge")
                code_challenge1()
                continue
            elif act01 == "2c":
                print(f"You've selected number {act01}")
                print("Welcome to my second code challenge")
                code_challenge2()
                continue
            elif act01 == "3c":
                print(f"You've selected number {act01}")
                print("Welcome to my third code challenge")
                code_challenge3()
                continue
            elif act01 == "4c":
                print(f"You've selected number {act01}")
                print("Welcome to my fourth code challenge")
                code_challenge4()
                continue
            elif act01 == "5c":
                print(f"You've selected number {act01}")
                print("Welcome to my fifth code challenge")
                code_challenge5()
                continue
            else:
                print("Invalid input...please, try again")
                continue

        elif act == "b": 
            print(f"You've selected letter {act}")
            print("Welcome to Code Challenges 6 to 10")
            print("Choose between the given options: ")
            print("6c - CodeChallenge6\n7c - CodeChallenge7\n8c - CodeChallenge8\n9c - CodeChallenge9\n10c - CodeChallenge10")
            act01 = input("Choose the following options:  ").lower()
            if act01 == "6c":
                print(f"You've selected number {act01}")
                print("Welcome to my sixth code challenge")
                code_challenge6()
                continue
            elif act01 == "7c":
                print(f"You've selected number {act01}")
                print("Welcome to my seventh code challenge")
                code_challenge7()
                continue
            elif act01 == "8c":
                print(f"You've selected number {act01}")
                print("Welcome to my eighth code challenge")
                code_challenge8()
                continue
            elif act01 == "9c":
                print(f"You've selected number {act01}")
                print("Welcome to my ninth code challenge")
                code_challenge9()
                continue
            elif act01 == "10c":
                print(f"You've selected number {act01}")
                print("Welcome to my tenth codechallenge")
                code_challenge10()
                continue
            else:
                print("Invalid input, try again")
                continue

        elif act == "c":
            print(f"You've selected letter {act}")
            print("Welcome to Code Challenges 11 to 15")
            print("Choose between the given options: ")
            print("11c - CodeChallenge11\n12c - CodeChallenge12\n13c - CodeChallenge13\n14c - CodeChallenge14\n15c - CodeChallenge15")
            act01 = input("Choose the following options:  ").lower()
            if act01 == "11c":
                print(f"You've selected number {act01}")
                print("Welcome to my eleventh code challenge")
                code_challenge11()
                continue
            elif act01 == "12c":
                print(f"You've selected number {act01}")
                print("Welcome to my twelfth code challenge")
                code_challenge12()
                continue
            elif act01 == "13c":
                print(f"You've selected number {act01}")
                print("Welcome to my thirteenth code challenge")
                code_challenge13()
                continue
            elif act01 == "14c":
                print(f"You've selected number {act01}")
                print("Welcome to my fourteenth code challenge")
                code_challenge14()
                continue
            elif act01 == "15c":
                print(f"You've selected number {act01}")
                print("Welcome to my fifteenth codechallenge")
                code_challenge15()
                continue
            else:
                print("Invalid input...please, try again")
                continue

        elif act == "d":
            print(f"You've selected letter {act}")
            print("Welcome to Code Challenge 16")
            print("Choose between the given options: ")
            print("16c - CodeChallenge16")
            act01 = input("Choose the following options:  ").lower()
            if act01 == "16c":
                print(f"You've selected number {act01}")
                print("Welcome to my sixteenth code challenge")
                code_challenge16()
                continue
            else:
                print("Invalid input, try again")
                continue

        elif act == "s": 
            print("The Program Stop")
            break
        else:
            print("Invalid input, choose only between the given choices.")
            continue