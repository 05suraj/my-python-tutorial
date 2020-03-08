# def addtion(n):
#     return n+n

# number=(1,2,3,4,5,6)
# result=map(addtion,number)
# print(list(result))


# todo------that is lamda in in line fun-----
# number = (1, 2, 3, 4, 5, 6)
# result=map(lambda x:x+x,number)
# print(list(result))

number1 = [1, 2, 3, 4]
number2 = [5, 6, 7, 8]
result = map(lambda x, y: x*y, number1, number2)
print(list(result))


l = ['suraj', 'niraj', 'ajay', 'saxena']
test = list((map(list, l)))
print(test)
