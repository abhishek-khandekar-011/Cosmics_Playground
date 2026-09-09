def fibonacci_Sequence(num):
    fib1 = 0
    fib2 = 1
    for i in range(num):
        next_num = fib1 + fib2
        fib1 = fib2
        fib2 = next_num
        print(fib1, end=" ")

number = int(input("Enter the number n upto which you want to generate the sequence: "))
print(f"The sequence upto {number} number(s) is: ")
fibonacci_Sequence(number)
