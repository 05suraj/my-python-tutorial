# def pattern(n):
#     for i in range(0, n):
#         for j in range(0, i + 1):
#             print("*", end="")
#         print("\r")


# n = 5
# pattern(n)


# num = int(input("chosre your number:"))

# for i in range(1, num + 1):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print("\r")

print("How Many Row You Want To Print")
one = int(input())
print("Type 1 Or 0")
two = int(input())
new = bool(two)
if new == True:

    for i in range(1, one+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()
elif new == False:
    for i in range(one, 0, -1):
        for j in range(1, i+1):
            print("*", end="")
        print()
