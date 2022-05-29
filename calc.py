import helpers.addition as add
import helpers.subtraction as minus
import helpers.division as divide
import helpers.multiplication as multiply


# welcome to the simple calculator, please select from the following options:

# 1. Add
# 2.Substract
# 3. Divide
# 4. multiply

# please enter your selection:

print("select an operation to perform: ")
print("1. add")
print("2. subtract")
print("3. divide")
print("4. multiply")

# please enter your first number:
# please enter your second number


action = input()

if action == "1":
    num1 = input("please enter first number: ")
    num2 = input("please enter second  number: ")
    print("the sum is " + (int(num1) + int(num2)))

elif action == "2":
    num1 = input("please enter first number: ")
    num2 = input("please enter second  number: ")
    print("the difference is " + (int(num1) - int(num2)))

elif action == "3":
    num1 = input("please enter first number: ")
    num2 = input("please enter second  number: ")
    print("the difference is " + (int(num1) / int(num2)))

elif action == "4":
    num1 = input("please enter first number: ")
    num2 = input("please enter second  number: ")
    print("the difference is " + (int(num1)  * int(num2)))
    
else: 
  print("Invalid Entry")


