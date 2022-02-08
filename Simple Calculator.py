# let's create a simple calculator using python:

# Function of performing Addition:
def add(x,y):
        return x + y
# Function of performing Substraction:
def sub(x,y):
        return x-y
# Function of performing Munltiplication:
def multi(x,y):
        return x*y
# Function of performing Division:
def divide(x,y):
        return x/y
# Options of performing:
print("Select Oparation :")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
while True:
        # Take input from user:
        choice = input("Enter the choice (1/2/3/4) :")
        # if choice is one of the four options:
        if choice in ("1","2","3","4"):
                num1 = float(input("Enter the first number :"))
                num2 = float(input("Enter the second number :"))
        if choice == "1":
                print(num1, "+", num2, "=", add(num1,num2))
        elif choice == "2":
                print(num1, "-", num2,"=",sub(num1,num2))
        elif choice == "3":
                print(num1, "*", num2,"=",multi(num1,num2))
        elif choice == "4":
                print(num1, "/", num2,"=",divide(num1,num2))
        else:
                print("Wrong choice!!!!")
        next_calculation = input("Let's do another calculation. yes/no :")
        if next_calculation == "no":
                                break
        else:
             print("Caculate again!!!!")