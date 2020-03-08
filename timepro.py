import time

initial = time.time()
k = 0
while(k < 45):
    k += 1
    print("this is while")
print("while loop run in ", time.time()-initial, "second")

initial2 = time.time()
for i in range(45):
    print("this is for loop")
print("for loops run in ", time.time()-initial2, 'second')


local_time = time.ctime()
print("local time ", local_time)

# todo...time.sleepself()

print("this is print ")

localtime = time.sleep(2.5)
print(localtime)

# todo get time..self.

result = time.gmtime(1454454647)
print("resut:", result)
print("\nyear:", result.tm_year)

print("tm_hour:", result.tm_hour)
