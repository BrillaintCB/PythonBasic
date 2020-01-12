def mulCal(jobtype, *args):
    if jobtype == "add":
        result = 0
        for i in args:
            result += i
    elif jobtype == "multiply":
        result = 1
        for i in args:
            result *= i
    return result

print(mulCal("add",2,4))
print(mulCal("multiply",2,4))
print(mulCal("multiply",2,6,8))


class Caldulator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
    def sub(self, num):
        self.result -+ num

