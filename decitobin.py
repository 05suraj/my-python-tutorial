def decimaltobinary(num):
    """this number is convert is  decimal to bunary and print it """
    if num > 1:
        decimaltobinary(num//2)
    print(num % 2, end="")


num = int(input("enter the num: "))
decimaltobinary(num)

