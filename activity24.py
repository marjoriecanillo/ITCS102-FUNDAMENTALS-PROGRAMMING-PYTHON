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