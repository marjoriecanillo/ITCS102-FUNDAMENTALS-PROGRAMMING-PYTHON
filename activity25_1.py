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