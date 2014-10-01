import arithmetic

def calculator(operator, *nums):
    num1, num2 = nums
    if operator == '+':
        print arithmetic.add(num1, num2)

    elif operator == '-':
        print arithmetic.subtract(num1, num2)

    elif operator == '*':
        print arithmetic.multiply(num1, num2)

    elif operator == '/':
        print arithmetic.divide(num1, num2)

    elif operator == 'square':
        print arithmetic.square(num1)

    elif operator == 'cube':
        print arithmetic.cube(num1)

    elif operator == 'pow':
        print arithmetic.power(num1, num2)

    elif operator == 'mod':
        print arithmetic.mod(num1, num2)

    else:
        print "Sorry, I don't understand."

def main():
    while True:
        input = raw_input()
        if input == "q":
            break    # return 
        else:
            input = input.split(' ')
            operator = input[0]
            num1 = int(input[1])
            if operator == 'square' or operator == 'cube':
                num2 = None
            else:
                num2 = int(input[2])
            calculator(operator, num1, num2)

        

if __name__ == '__main__':
    main()