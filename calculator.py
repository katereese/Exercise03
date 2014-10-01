def calculator(operator, num1, num2):
    if operator == '+':
        print add(num1, num2)

    elif operator == '-':
        print subtract(num1, num2)

    elif operator == '*':
        print multiply(num1, num2)

    elif operator == '/':
        print divide(num1, num2)

    elif operator == 'square' and num2 == 2:
        print square(num1, num2)

    elif operator == 'cube' and num2 == 3:
        print cube(num1, num2)

    elif operator == 'pow' and num2 != 2 and num2 != 3:
        print power(num1, num2)

    elif operator == 'mod':
        print mod(num1, num2)

    else:
        print "Sorry, I don't understand."

def process_and_run():
    while True:
        input = raw_input()
        if input == "q":
            break
        else:
            input = input.split(' ')
            operator = input[0]
            num1 = int(input[1])
            num2 = int(input[2])
            calculator(operator, num1, num2)
        

process_and_run()