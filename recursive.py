# houses = ['suraj', 'ritu', 'suraj', 'ritu', 'suraj', 'ritu']


# def deliver_presents_iterative():
#     for house in houses:
#         print("deleviring presents to : ", house)


# deliver_presents_iterative()

# todo....new

# def deliver_presents_iterative(houses):
#     if len(houses) == 1:
#         house = houses[0]
#         print("delivering presents to ", house)
#     else:
#         mid = len(houses) // 2
#         frist_half = houses[:mid]
#         second_half = houses[mid:]
#         deliver_presents_iterative(frist_half)
#         deliver_presents_iterative(second_half)


# deliver_presents_iterative(houses)


# todo...fibonacci...


# def fibonacci(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
# fibonacci(5)
# login  of factorial
'''4!=find the factorial of this number

formula is n!=n*(n-1)*(n-2)*(n-3)*.....*1


'''

# todo..factorial


def factorial(num):
    if num == 1:
        return num
    else:
        return num*factorial(num-1)


num = int(input("enter ther number :"))

print(factorial(num))


n = 5
fact = 1
for i in range(1, n+1):
    fact = fact*i
print("thete factorial  number 20  is :", end="")
print(fact)
