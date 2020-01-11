
class CoreCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setDate(self, first ,second):
        self.first = first
        self.second = second

    #def sum(self, first, second):
    #    return first + second

    def sum(self):
        return self.first + self.second

    #def sub(self, first, second):
    #    return first - second

    def sub(self):
        return self.first - self.second

    #def multiply(self, first, second):
    #    return first * second

    def multiply(self):
        return self.first * self.second

    #def devide(self, first, second):
    #    if second != 0:
    #        return first / second

    def devide(self):
        if self.second != 0:
            return self.first / self.second
#a = CoreCal()
#a.setDate(3,4) 

#b = CoreCal()
#b.setDate(5,7)

# With __init__

a = CoreCal(3,4)
b = CoreCal(5,7)

print(type(a))
print(id(a.first))
print(id(a.second))
print(id(b.first))
print(id(b.second))
print(a.first, a.second)

#print(a.sum(5,4))
#print(a.sub(5,4))
#print(a.multiply(5,4))
#print(a.devide(5,0))


# With __init__

print(a.sum())
print(a.sub())
print(a.multiply())
print(a.devide())

class AdditionalCal(CoreCal):
    def pow(self):
        result = self.first ** self.second
        return result

    #method overriding
    def devide(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
            

ad = AdditionalCal(5,4)
print(type(b))


print(ad.pow())

ad1 = AdditionalCal(5,0)
print(ad1.devide())