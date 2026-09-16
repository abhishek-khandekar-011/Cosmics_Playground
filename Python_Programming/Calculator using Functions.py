
def add (n1, n2):
    return n1 + n2
def sub (n1, n2):
    return n1 - n2
def multiply (n1, n2):
    return n1 * n2
def division (n1 , n2):
    return n1 / n2

operation = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/" : division,
}

def calculator():
    num1 = float(input("Enter the first number: "))
    should_continue = True
    while should_continue:
        for symbols in operation:
            print(symbols)
        operator = str(input("Enter the operator: "))
        num2 = float(input("Enter the next number: "))
        result = operation[operator](num1,num2)
        print(f"The result is {result}")
        cont = str(input("Enter Y if you want to start new calculation else enter n to continue existing calculations: ")).lower()
        if cont == "y":
            num1 = result
        else:
            print("/n*20")
calculator()
