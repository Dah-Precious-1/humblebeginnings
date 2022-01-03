import sys

print("Welcome to the calculator\n"
              "\t(+): Addition\n"
              "\t(-): Subtraction\n"
              "\t(/): Division\n"
              "\t(*): Multiplication\n"
              "\t(**): raise to power\n")
def calculate():
    return play_again()

def play_again():
    number1 = eval(input("\nEnter a number: "))
    running = True
    while running:
        symbol = input("\nEnter a symbol\n")
        
        number2 = eval(input("\nEnter a number: "))
        if symbol == "+":
            number1 = number1 + number2
            print("\nyour result is ", number1)
        elif symbol == "-":
            number1 = number1 - number2
            print("\nyour result is ", number1)
        elif symbol == "/":
            number1 = number1 / number2
            print("\nyour result is ", number1)
        elif symbol == "*":
            number1 = number1 * number2
            print("\nyour result is ", number1)
        elif symbol == "**":
            number1 = number1 ** number2
            print("\nyour result is ", number1)
            
        return play_again()

        
calculate()
