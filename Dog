class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialized Dog :{}'.format(self.name))

    def bark(self):
        print('Dog Name :{} Dog Age :{} '.format(self.name,self.age), end= "")

class Shannoyed:
    def __init__(self, name, age, gender, child):
        Dog.__init__(self, name, age)
        self.gender = gender
        self.child = child

    def bark(self):
        Dog.bark(self)
        print('Gender : {}  Child : {:d}'.format(self.gender,self.child))

class GoldenRetiever:
    def __init__(self, name, age, gender, child):
        Dog.__init__(self, name, age)
        self.gender = gender
        self.child = child

    def bark(self):
        Dog.bark(self)
        print('Gender : {}  Child : {}'.format(self.gender,self.child))


class Huskey:
    def __init__(self, name, age, gender, child, master):
        Dog.__init__(self, name, age)
        self.gender = gender
        self.child = child
        self.master = master

    def bark(self):
        Dog.bark(self)
        print('Gender : {}  Child : {} Master: {}'.format(self.gender, self.child, self.master))

s = Shannoyed('Bo Bo', 5, 'Male', 10)
g = GoldenRetiever('Shaung Shaung', 6, 'Female', 9)
h = Huskey('Ki Ki', 7, 'Male',7,2)

print()

dogfamily= [s, g, h]

for dog in dogfamily:
    dog.bark()