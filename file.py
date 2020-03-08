# f = open("suraj.txt")
# content = f.read()
# print(content)

# f.close()

# f = open("sony.txt", "r+")
# # f.write("suraj is a good boy and sony also ")
# print(f.read())
# f.write("thank you")


# f.close()


# todo,seek()  and tell()

# f = open("suraj.txt")
# print(f.tell())
# print(f.readline())
# f.seek(1)
# print(f.readline())
# f.close()


# Python code to
# demonstrate readlines()

# import datetime


# def gettime():
#     return datetime.datetime.now()


# def take(k):
#     if k == 1:
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if(c == 1):
#             value = input("type here\n")
#             with open("harry-ex.txt", "a") as op:
#                 op.write(str([str(gettime())])+": "+value+"\n")
#             print("successfully written")
#         elif(c == 2):
#             value = input("type here\n")
#             with open("harry-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     elif(k == 2):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("rohan-ex.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("rohan-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     elif(k == 3):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("hammad-ex.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("hammad-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     else:
#         print("plz enter valid input (1(harry),2(rohan),3(hammad)")


# def retrieve(k):
#     if k == 1:
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if(c == 1):
#             with open("harry-ex.txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif(c == 2):
#             with open("harry-food.txt") as op:
# #                 for i in op:
# #                     print(i, end="")
# #     elif(k == 2):
# #         c = int(input("enter 1 for excersise and 2 for food"))
# #         if (c == 1):
# #             with open("rohan-ex.txt") as op:
# #                 for i in op:
# #                     print(i, end="")
# #         elif (c == 2):
# #             with open("rohan-food.txt") as op:
# #                 for i in op:
# #                     print(i, end="")
# #     elif(k == 3):
# #         c = int(input("enter 1 for excersise and 2 for food"))
# #         if (c == 1):
# #             with open("hammad-ex.txt") as op:
# #                 for i in op:
# #                     print(i, end="")
# #         elif (c == 2):
# #             with open("hammad-food.txt") as op:
# #                 for i in op:
# #                     print(i, end="")
# #     else:
# #         print("plz enter valid input (harry,rohan,hammad)")


# # print("health management system: ")
# # a = int(input("press 1 for lock the value and 2 for retrieve "))

# # if a == 1:
# #     b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
# #     take(b)
# # else:
# #     b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
# #     retrieve(b)

# # fname = input("Enter the name of the file:")
# import os

# # fname = input("enteter file name:")
# # if os.path.isfile(fname):
# #     infile = open(fname, 'r')
# #     lines = 0
# #     words = 0
# #     characters = 0
# #     for line in infile:
# #         wordslist = line.split()
# #         lines = lines + 1
# #         words = words + len(wordslist)
# #         characters = characters + len(line)
# #     print(lines)
# #     print(words)
# #     print(characters)
# # else:
# #     print("file dose exixt ")file

# filename = input('enter the name of file:')
# isfileis_in_folder = (filename, 'r')
# if "s" in isfileis_in_folder:
#     print('is there')
# else:
#     textlines = 0
#     textworld = 0
#     textcharacter = 0
#     for line in isfileis_in_folder:
#         textworld_list = line.split()
#         textlines = textlines+1
#         textworld = textworld+len(textworld_list)
#         textcharacter = textcharacter+len(line)

# print(textworld)

# list = [i*i for i in range(20) if i % 2 == 0]

# print(list)

list = [2, 3, 56, 4, 6, 4, 2, 2, 2, 2]
for i in range(30):
    if i % 2 == 0:
        print(i)
