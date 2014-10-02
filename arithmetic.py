def add(*nums):
    summation = 0
    for i in nums:
        summation = summation + int(i)
    return summation

def subtract(*nums):
    diff = int(nums[0])
    for i in nums[1:]:
        diff = diff - int(i)
    return diff

def multiply(*nums):
    product = 1
    for i in nums:
        product = product * int(i)
    return product

def divide(*nums):
    quotient = float(nums[0])
    for i in nums[1:]:
        if float(i) == 0:
            return "Error! You cannot divide by zero!"
        else:
            quotient = quotient / float(i)
            return quotient

def square(*nums):
    num1 = nums
    return int(num1) ** 2

def cube(*nums):
    num1 = nums
    return int(num1) ** 3

def power(*nums):
    num1, num2 = nums
    return int(num1) ** int(num2)

def mod(*nums):
    num1, num2 = nums
    return int(num1) % int(num2)
