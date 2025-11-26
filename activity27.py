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