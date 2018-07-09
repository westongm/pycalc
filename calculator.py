
#need to receive args from user
import addition.py
#process args, includes validation
#valiate and convert nums to ints
#validate operators
#eventually run it in a loop until user quits program
#create a gui

def calc (numa, oper, numb):
    operators = ['-', '+','*', '/']
    num1 = int(numa)
    num2 = int(numb)
    if oper not in operators :
        print ("please use a valid operator")
        exit(1)
    if oper == '+':
        print(num1 + num2)
    elif oper == '-':
        print(num1 - num2)
    elif oper == '*':
            print(num1*num2)
    elif oper =='/':
            print(num1/num2)
    #exit(0)
    

#calc('1', '+','2')  

#calc(3, '/', 2)  
numa = input("Enter first number: ")

oper = raw_input("Enter Operator: ")

numb = input ("Enter second number: ")

calc(numa, oper, numb)

