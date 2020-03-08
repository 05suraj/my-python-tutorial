class Student:
    my_age = 5
    pass


suraj = Student()
sony = Student()

suraj.name = "kumar"
suraj.std = 12
suraj.section = 1
sony.name = 'vish'
list = ["mango", 'banaa', 'that', 'orenge']
for i in list:

    print(list)


print(suraj.name, sony.name)
print(sony.name)
print(
    f"my name is suraj  kumar{suraj.name} tere  age of  {suraj.std}  that is full list {list} ")

print(suraj.my_age)

print(Student.__dict__)
