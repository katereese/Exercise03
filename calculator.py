import arithmetic

def calculator(operator, *nums):

    if operator == '+':
        return arithmetic.add(*nums)

    elif operator == '-':
        return arithmetic.subtract(*nums)

    elif operator == '*':
        return arithmetic.multiply(*nums)

    elif operator == '/':
        return arithmetic.divide(*nums)

    elif operator == 'square':
        if len(nums) == 1:
            return arithmetic.square(*nums)
        else:
            return "Input must be one number."

    elif operator == 'cube':
        if len(nums) == 1:
            return arithmetic.cube(*nums)
        else:
            return "Input must be one number."

    elif operator == 'pow':
        if len(nums) == 2:
            return arithmetic.power(*nums)
        else:
            return "Input must be two numbers."

    elif operator == 'mod':
        if len(nums) == 2:
            return arithmetic.mod(*nums)
        else:
            return "Input must be two numbers."

    else:
        return "Sorry, I don't understand."

def main():
    while True:
        input = raw_input()
        if input == "q":
            break    # return 
        else:
            input = input.split(' ')
            operator = input[0]
            nums = input[1:]
            print calculator(operator, *nums)

        
if __name__ == '__main__':
    main()