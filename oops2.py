class Employee:
    no_of_leave = 8

    def printdetaile(self):
        return f"name  is {self.name} and age is{self.age} and sailrery is{self.sailery}"


suraj = Employee()
sony = Employee()

suraj.name = "suraj saxena"
suraj.sailery = 12777
suraj.age = 24

sony.name = 'vish'
sony.sailery = 1200
sony.age = 22
print(sony.printdetaile())
 