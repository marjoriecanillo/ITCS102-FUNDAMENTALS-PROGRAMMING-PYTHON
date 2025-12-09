#Activities
def activity1():
    print("Hello World")

def activity2():
    name = input("What is your name .? ")

    print("Hi", name , "Welcome to the Matrix") 

def activity3():
    #print("Happy\n\t\tMonday, ")
    #print("\t\tBSIT 1A \n from DLL")
    print("The Quick Brown \rJumps over the Lazy Dog.")

def activity4():
    name =input("Enter a string-> ")
    print("Your name has ",len(name), "characters")

def activity5():
    something =eval(input("Input something -->"))
    print("The data type of something is",type(something))

def activity6():  
    n1 =eval(input("Enter the first number : "))
    n2 =eval(input("Enter the second number : "))

    s = n1 + n2
    d = n1 - n2
    p = n1 

    n1 =eval(input("Enter the first number : "))
    n2 =eval(input("Enter the second number : "))

    s = n1 + n2
    d = n1 - n2
    p = n1 * n2
    q = n1 / n2

    print("The sum of",n1,"and",n2,"is",s)
    print("The difference of",n1,"and",n2,"is",d)
    print("The product of",n1,"and",n2,"is",p)
    print("The qoutient of",n1,"and",n2,"is",q)
    print(n1, "exponent by",n2,"is",n1**n2)
    print("The remainder of",n1,"and",n2,"is",n1 % n2)
    print("The floor division of",n1,"and",n2,"is",n1//n2) 

def activity7():   
    a = 5

    print("the value of a is ", a)

    a = a + 5
    a += 3
    a += 8
    a *= 2
    a -= 3

    print("the value of a is ", a)

def activity8():
    balance = 500
    withdrawal = 1500
    b = 3
    a = 3
    name1 = 'marjorie'
    name2 = 'Marjorie'
    print(b >= a )
    print(name1 != name2)

def activity9():
    username = 'marjorie'
    password = '2025'

    print(username == 'marjorie' )
    print((username == 'marjorie' ) and (password == '2025' ))
    print((username == 'marjorie' ) or (password == '2025' ))

def activity10():
    name = input("Input your name ---> ")
    isStudent = input("Are you a student (Yes / No) --> ")
    fare = eval(input("bayad --> "))

    if isStudent.lower() == "yes":
        discount = fare * .2
        new_fare = fare - discount
        print("Hi", name, " student discount is ", discount, "Discounted fare is ", new_fare)
    else:
        print("Sorry ", name," you are not eligible for student discount")

def activity11():
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

def activity12():
    for ikot in range(1, 11, 1):
	print('hello world')

def activity13():
    num = 0
    for y in range(1, 11):
        number = eval(input("Enter a number "))
        num += number
        print('bagong value ni num ay',num)
    print(num)

def activity14():
    for y in range(20, 0, -1):
	print(y)

def activity15():
    firstname = 'marjorie'
    lname = 'canillo'

    print(f"My name is {firstname.upper()} {lname.upper()}")

def activity16():
    for y in range(1,11,1):
	print(y,end="")

def activity17():
    for y in range(1,11,1):
	for x in range(1,11,1):
	 print(x,end=" ")
	print()

def activity18():
    for y in range(1,11,1):
	for x in range(1, y, 1):
	 print(x, end=' ')
	print()

def activity19():
    for y in range(1,11,1):
	for x in range(1, y, 1):
	 print("*", end=' ')
	print()

def activity20():
    for y in range(1,11,1):
	#for x in range(1, y, 1):
	 #print(" ", end=' ')
	for i in range(10, y, -1):
	 print("*",end= " ")
	print()

def activity21():
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

def activity22():
    import random
    print("Welcome to the Number Guessing Game!")
    random_number = random.randint(1, 20)
    trial = 0
    cont = True

    while cont == True:
    guess = int(input("Guess a number between 1 and 20: "))
    trial += 1
    if guess < random_number:
        print("Too low! Try again.")
        continue
    elif guess > random_number:
        print("Too high! Try again.")
        continue
    elif guess == random_number:
        print(f"Congratulations! You've guessed the number {random_number} in {trial} tries.")
        break

def activity23():
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

def activity24():
    #creating your own function
    #keyword , def - define
    #the content inside the parenthesis is called
    #CODE RESUABILITY

    def greeter(name):
        print(f"Hi {name}, how have you been? ")

    def summation(y):
        sum = 0
        for i in range(y, 0, -1):
            sum += i
        print(f"The sum of {y} is {sum}") 

    greeter("jo")
    greeter("cande")
    summation(15)
    summation(9)
    summation(17)

def activity24_1():
    from activity24 import greeter,summation

    greeter("marjo")
    greeter("mando")
    summation(50)
    summation(100)

def activity25():
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

def activity25_1.py():
    def activity1():
    print("Hello World!")

    def activity2():
    answer=input("who is the greatest singer? ")
    print("Is that even a question?? You know there's only one right answer, and it's", answer)
    def code_challenge1():
    name=input("Type your name: ")
    print("\t\t\t*\n\n\t\t*\t\t*\n\n\t*\t\t\t\t*\n\n*\t\t  hi, ", name, "\t\t*\n\n\t*\t\t\t\t*\n\n\t\t*\t\t*\n\n\t\t\t*")
    def code_challenge2():
    x = eval(input("Enter the amount you want to deposit: "))
    print("\nHere is a detailed breakdown in PH currency:")
    print("\n1000 --" ,x//1000)
    print("500  --" ,((x%1000)//500))
    print("200  --" ,(((x%1000)%500)//200))
    print("100  --" ,((((x%1000)%500)%200)//100))
    print("50   --" ,((((x%1000)%500)%200)%100)//50)
    print("20   --" ,(((((x%1000)%500)%200)%100)%50)//20)
    print("10   --" ,((((((x%1000)%500)%200)%100)%50)%20)//10)
    print("5    --" ,(((((((x%1000)%500)%200)%100)%50)%20)%10)//5)
    print("1    --" ,((((((((x%1000)%500)%200)%100)%50)%20)%10)%5)//1)
    print("Total amount:" ,x)

    #call your function here
    activity2()
            
def activity26():
    genre = ['romcom', 'drama', 'horror', 'comedy', 'romance', 'action']

    print(genre[5])

def activity27():
    print("Adding Data to Dictionary")
    print(" =================================")
    cont = True

    empty_dictionary = {}

    def print_movie():
        for x,n in empty_dictionary.items():
            print(f"Code {x} Title -- {n}")

    while cont == True:
    keys = input("Input keys for your movie: ")
    value = input("Enter movie title: ")

    empty_dictionary[keys] = value

    choice = input("Do you like adding more \ny-Yes\nn-No\np-print\n --> ").lower()

    if choice == 'y':
        print("continuing...")
        continue
    elif choice =='n':
        print("Stop the Program")
        continue
    elif choice == 'p':
        print_movie()
        continue
    else:
        print("invalid choice")
        break

def activity28():
    #Step 1 
    import pygame
    import time
    import random

    # Initialize Pygame
    pygame.init()

    # Screen size
    width = 600
    height = 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game')

    # Colors (RGB)
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)

    # Game speed and block size
    clock = pygame.time.Clock()
    speed = 10
    snake_block = 10

    # Font for messages
    font_style = pygame.font.SysFont(None, 30)


    #Step 2 
    def draw_snake(snake_list):
        for block in snake_list:
            pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

    #Step 3 
    def game_loop():
        game_over = False
        game_close = False

        # Starting position of the snake
        x = width / 2
        y = height / 2

        x_change = 0
        y_change = 0

        snake_list = []
        length_of_snake = 1

        # Generate first food
        food_x = round(random.randrange(0, width - snake_block) / 10) * 10
        food_y = round(random.randrange(0, height - snake_block) / 10) * 10

        while not game_over:

            # Loss screen
            while game_close:
                screen.fill(black)
                message = font_style.render('You Lost! Press Q-Quit or C-Play Again', True, red)
                screen.blit(message, [width / 6, height / 3])
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        elif event.key == pygame.K_c:
                            game_loop()

            # Event handling (keyboard)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -snake_block
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = snake_block
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        y_change = -snake_block
                        x_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = snake_block
                        x_change = 0

            # Check if snake hits the wall
            if x >= width or x < 0 or y >= height or y < 0:
                game_close = True

            # Update position
            x += x_change
            y += y_change

            # Draw background and food
            screen.fill(black)
            pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

            # Add snake head
            snake_head = [x, y]
            snake_list.append(snake_head)

            # Remove extra segments if not growing
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            # Check self-collision
            for segment in snake_list[:-1]:
                if segment == snake_head:
                    game_close = True

            # Draw the snake
            draw_snake(snake_list)

            # Update display
            pygame.display.update()

            # Check if snake eats food
            if x == food_x and y == food_y:
                food_x = round(random.randrange(0, width - snake_block) / 10) * 10
                food_y = round(random.randrange(0, height - snake_block) / 10) * 10
                length_of_snake += 1

            # Control game speed
            clock.tick(speed)

        # Quit Pygame
        pygame.quit()
        quit()

    # Start the game
    game_loop()



#Code Challenges
def code_challenge1():
    name = input("What's your name: ")

    print("\t\t\t\t\t*\n\t\t\t\t*\t\t*\n\t\t\t*\t\t\t\t*\n\t\t*\t\t\tHi\t\t\t*\n\t*\t\t\t",name,"\t\t\t\t*\n\t\t*\t\t\t\t\t\t*\n\t\t\t*\t\t\t\t*\n\t\t\t\t*\t\t*\n\t\t\t\t\t*")

def code_challenge2():
    n1 =int(input("Enter amount to deposit : "))
    n2 =int(input("Enter the number of 1000 deposit : "))
    n3 =int(input("Enter the number of 500 deposit : "))
    n4 =int(input("Enter the number of 200 deposit : "))
    n5 =int(input("Enter the number of 100 deposit : "))
    n6 =int(input("Enter the number of 50 deposit : "))
    n7 =int(input("Enter the number of 20 deposit : "))
    n8 =int(input("Enter the number of 10 deposit : "))
    n9 =int(input("Enter the number of 5 deposit : "))
    n10 =int(input("Enter the number of 1 deposit : "))

    a = n2 * 1000
    b = n3 * 500
    c = n4 * 200
    d = n5 * 100
    e = n6 * 50
    f = n7 * 20
    g = n8 * 10
    h = n9 * 5
    i = n10 * 1

    total = a + b + c + d + e + f + g + h + i

    print("Total from denominations: ", total) 

def code_challenge3():
    username = "marjorie"
    pwd = "123456"

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "marjorie"and password == "123456":
        print("Access Granted")
    else:
        print("Access Denied")

def code_challenge4():
    number = eval(input("Enter a number: "))

    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

def code_challenge5():
    print("Welcome to the Manga Recommender! ")
    print("Answer a few questions to find your next read.")
    genre = input("What genre do you like? (action, romance): ")
    length = input("How long should the manga be? (short, medium, long): ")
    decade = input("Which decade? (2010s, 2020s): ")

    if genre == "action":
        if length == "short" and decade == "2010s":
        print("Recommendation: Samurai Girls")
        elif length == "short" and decade == "2020s":
        print("Recommendation: Tower of God")
        elif length == "medium" and decade == "2010s":
        print("Recommendation: Katanagatari")
        elif length == "medium" and decade == "2020s":
        print("Recommendation: Decadence")
        elif length == "long" and decade == "2010s":
        print("Recommendation: Hakuoki")
        elif length == "long" and decade == "2020s":
        print("Recommendation: Jujutsu Kaisen")
        else:
        print("Sorry, no action manga matches your selection.")

    elif genre == "romance":
        if length == "short" and decade == "2010s":
        print("Recommendation: Kimi ni Todoke")
        elif length == "short" and decade == "2020s":
        print("Recommendation: Kubo Won't Let Me Be Invisible")
        elif length == "medium" and decade == "2010s":
        print("Recommendation: Maid Sama!")
        elif length == "medium" and decade == "2020s":
        print("Recommendation: My Dress-Up Darling")
        elif length == "long" and decade == "2010s":
        print("Recommendation: Angel Beats!")
        elif length == "long" and decade == "2020s":
        print("Recommendation: The Quintessential Quintuplets")
        else:
        print("Sorry, no romance manga matches your selection.")

    else:
        print("Invalid genre. Please choose from 'action', or 'romance'.")

def code_challenge6():
    num = eval(input("Input a number --> "))

    result = 1
    for y in range(num, 0, -1):
        result *= y

    print("Factorial is ",result)

def code_challenge7():
    num = 0
    for y in range(1, 11, 1):
        number = eval(input("Input number: "))
        if number % 2:
        num += number
    print("The sum of all the ODD number is ",num)

def code_challenge8():
    print("MULTIPLICATION TABLE MAKER")
    number = int(input("Enter a number: "))

    for y in range(1, 11):
        mul = number * y
        print(number, "x", y, "=", mul)

def code_challenge9():
    print("COUNTDOWN TIMER SIMULATOR")
    countdown = int(input("Enter the starting number for countdown: "))
    print("Countdown started: ")

    for y in range(countdown, 0, -1):
        print(y)
    print("Liftoff! ")

def code_challenge10():
   #print("\t\t *",end=" ")
    for y in range(1, 11, 1):
	for x in range(10, y, -1):
	  print(" ",end =' ')
	for i in range(1, y, 1):
	  print("*", end =' ')
	for z in range(1, y, 1):
	 print("*", end =' ')
	print()

def code_challenge11():
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

def code_challenge12():
    for me in range(1,7,1):
	for us in range(7,me,-1):
	 print(" ", end=' ')
	for you in range(me,0,-1):
	 print(you, end=' ')
	for them in range(2,me+1):
	 print(them, end=' ')
	print()

def code_challenge13():
        print("\t\t\t               *")
    for z in range(1,2,1):
        for d in range(20,z,-1):
            print(" ", end=" ")
        for r in range(0,z,1):
            print("*", end=' ')
        for y in range(0,z,1):
            print("*", end=" ")
        print()
    for b in range(3,1,-1):
            for f in range(b,21,1):
                print(" ", end=' ')
            for g in range(b,1,-1):
                print("*", end=' ')
            for h in range(b,1,-1):
                print("*", end=' ')
            print()
    print("\t\t\t               *")
    for i in range(1,11,1):
        for m in range(20,i,-1):
            print(" ", end=" ")
        for y in range(0,i,1):
            print("*", end=' ')
        for f in range(0,i,1):
            print("*", end=" ")
        print()
    for a in range(1,15,1):
        for b in range(20,a,-1):
            print(" ", end=" ")
        for t in range(0,a,1):
            print("*", end=' ')
        for w in range(0,a,1):
            print("*", end=" ")
        print()
    for o in range(1,7,1):
        for t in range(1,18,1):
            print(" ", end=' ')
        for w in range(1,7,1):
            print("*", end=' ')
        print()

def code_challenge14():
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

def code_challenge15():
        anime_list = []
    while True:
        anime_title = input("Enter the title of an anime (or type 'exit' to finish): ")

        if anime_title.lower() == 'exit':
        print("You have exited the anime entry program.")
        break

        anime_list.append(anime_title)
        print(f"'{anime_title}' has been added to your anime list.")

        print("Your anime list:", anime_list)

def codechallenge16():
    import os
    import json

    print("STUDENT INFORMATION SYSTEM")
    print("--------------------------------")
    student_records = {}

    while True:
        print("SELECT FROM THE CHOICES BELOW.\nA - Add information\nB - Print all records\nC - Search a record\nD -Delete a record\nE - Edit a record\nF - Exit")
        choice = input("Your choice --> ").lower()
        if choice == 'a':
            print("ADDING STUDENT INFORMATION")
            print("--------------------------")
            student_id = input("Enter student id: ")
            first_name = input("Enter first name: ").upper()
            last_name = input("Enter last name: ").upper()
            course = input("Enter course: ").upper()
            email = input("Enter email: ")
            student_records[student_id] = [first_name, last_name, course, email]
            print("Student information added successfully.\n")
            os.system('cls') 
            continue
        elif choice == 'b':
            print("PRINTING STUDENT RECORDS")
            print("-----------------------")
            for id, records in student_records.items():
                print("-----------------------")
                print(f"Student ID: {id} : {records}")
                print("-----------------------")
            continue    
        elif choice == 'c':
            os.system('cls')
            print("SEARCH STUDENT RECORD")  
            print("---------------------")
            search_id = input("Enter student id to search: ")
            if search_id in student_records:
                print("---------------------")
                print("\nRECORD FOUND.\n")
                print("---------------------")
            else:
                print("---------------------")
                print("\nRECORD NOT FOUND.\n")
                print("---------------------")
            continue
        elif choice == 'd':
            print("DELETE STUDENT RECORD")  
            print("---------------------")
            search_id = input("Enter student id to delete: ")
            if search_id in student_records:
                print("---------------------")
                print("\nRECORD FOUND.\n")
                print("---------------------")
                for a in student_records[search_id]:
                    print(f"-- {a}")
                student_records.pop(search_id)
                print("RECORD DELETED")
            else:
                print("---------------------")
                print("\nRECORD NOT FOUND.\n")
                print("---------------------")
            continue
        elif choice == 'e':
            os.system('cls')
            print("EDIT STUDENT RECORD")  
            print("---------------------")
            search_id = input("Enter student id to edit: ")
            if search_id in student_records:
                print("---------------------")
                print("\nRECORD FOUND.\n")
                print("---------------------")
                for a in student_records[search_id]:
                    print(f"-- {a}")
                print("Enter new details:")
                first_name = input("Enter first name: ").upper()
                last_name = input("Enter last name: ").upper()
                course = input("Enter course: ").upper()
                email = input("Enter email: ")
                student_records[search_id] = [first_name, last_name, course, email]
                print("RECORD UPDATED")
                
            else:
                print("---------------------")
                print("\nRECORD NOT FOUND.\n")
                print("---------------------")
            continue

        elif choice == 'f':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
            continue