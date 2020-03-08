# x = 5


# def functions():
#     global x
#     y = "local variable"
#     # x=6
#     x = x * 5
#     print(y)
#     print(x)


# functions()

x = 50


def suraj():
    x = 20

    def sony():
        x = 90
        print("before calling suraj", x)
    sony()
    print("after calling sony", x)


suraj()
print(x)
