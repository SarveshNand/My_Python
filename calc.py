def cal(operand1, operand2, operator):
    if operator == "+":
        return add(operand1, operand2)
    
    if operator == "-":
        return sub(operand1, operand2)
    
    if operator == "*":
        return mul(operand1, operand2)
    
    if operator == "/":
        return div(operand1, operand2)
    
    if operator == "^":
        return power(operand1, operand2)
    
    return "Invalid Operator!"

def add(operand1, operand2):
    return operand1 + operand2

def sub(operand1, operand2):
    return operand1 - operand2

def mul(operand1, operand2):
    return operand1 * operand2

def div(operand1, operand2):
    if operand2 != 0:
        return operand1 / operand2
    else:
        return "Cannot divide by zero."

def power(operand1, operand2):
    return operand1 ** operand2

while True:
    operand1_input = input("Enter first operand (or X to exit): ")
    if operand1_input.lower() == "x":
        print("Calculator Exiting...")
        break

    operand2_input = input("Enter second operator: ")
    operator = input("Enter operator (+, -, *, /, ^): ")

    try:
        operand1 = int(operand1_input)
        operand2 = int(operand2_input)
        result = cal(operand1, operand2, operator)
        print("Result: ", result)
    
    except ValueError:
        print("Invalid input! Enter a Valid Number")