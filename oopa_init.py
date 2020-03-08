class Employee:
    no_of_leave = 23

    def __init__(self, aname, asailery, arole):
        self.name = aname
        self.sailary = asailery
        self.role = arole

    def printdetails(self):
        return f"my  name is {self.name} and my sailary is {self.sailary} my role is {self.role}"

# todo  '''here we can change the class var using this this mathod'''

    @classmethod
    def change_leaves(cls, newlwave):
        cls.no_of_leave = newlwave


suraj = Employee("sony", 2555, "webdeveloper")

suraj.change_leaves(56)

print(suraj.no_of_leave)
