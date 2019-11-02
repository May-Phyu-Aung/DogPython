import self as self


# class Person:
#     def __init__(self,name):
#         self.name = name
#
#     def say_hi(self):
#         print('Hello, my name is ', self.name)
#
# p = Person('May Phyu')
# p.say_hi()

# class Dog:
#     def __init__(self,name):
#         self.name = name
#
#     def say_hi(self):
#         print('Dog name is',self.name)
#     def eat(self):
#         print(self.name,'eat bone')
#
#     def bark(self):
#         print('Dog Bark')
#
# dog = Dog('Nga Nga')
# # dog.color('Black')
# # dog.owner('U Kaung')
# dog.say_hi()
# dog.eat()
# dog.bark()

# class Robot:
#     population = 0
#
#     def __init__(self,name):
#         self.name = name
#
#         print("(Initialization{})".format(self.name))
#
#         Robot.population += 1
#
#     def die(self):
#         print("{} is being destroyed!".format(self.name))
#         Robot.population -= 1
#
#         if Robot.population == 0:
#             print("{} was the last one.".format(self.name))
#         else:
#             print("There are still {:d} robots working.".format(Robot.population))
#
#     def say_hi(self):
#         print("Greetings, my sisters call me{}.".format(self.name))
#
#     @classmethod
#     def how_many(cls):
#         print("We have {:d} robots.".format(cls.population))
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# Robot.how_many()
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# Robot.how_many()
#
# droid3 = Robot('Q35')
# droid3.say_hi()
# droid3.how_many()
#
# print("\n Robots can do some work here.\n")
# print("Robots have finished their work.so let's destroy them")
# droid1.die()
# droid2.die()
# droid3.die()
#
# Robot.how_many()



# class Dog:
#     population = 0
#
#     def __init__(self,name):
#         self.name = name
#
#         print('(Initialization {}'.format(self.name))
#
#         Dog.population += 1
#
#     def die(self):
#         print("{} is being run".format(self.name))
#         Dog.population -= 1
#
#         if Dog.population == 0:
#             print("{} is the last dog".format(self.name))
#         else:
#             print("There are still {} dogs eating".format(Dog.population))
#
#     def say_hi(self):
#         print("This dog name is {}".format(self.name))
#
#     @classmethod
#     def how_many(cls):
#         print("We have {} dogs".format(cls.population))
#
# dog1 = Dog("Nga")
# dog1.say_hi()
# dog1.how_many()
#
# dog2 = Dog("Nga1")
# dog2.say_hi()
# dog2.how_many()
#
# dog3 = Dog("Nga2")
# dog3.say_hi()
# dog3.how_many()
#
# print("Dog can eat")
#
# print("Dogs have eaten food.so let's escape them")
#
# dog1.die()
# dog2.die()
# dog3.die()


# class SchoolMember:
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print('(Initialized SchoolMember: {})'.format(self.name))
#
#     def tell(self):
#         print('Name:"{}" Age:"{}"'.format(self.name, self.age), end="")
#
# class Teacher(SchoolMember):
#
#     def __init__(self, name, age, marks):
#         SchoolMember.__init__(self, name, age)
#         self.marks = marks
#         print('(Initialized Teacher:{})'.format(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print('Marks: "{:d}"'.format(self.marks))
#
# class Student(SchoolMember):
#     def __init__(self, name, age, marks):
#         SchoolMember.__init__(self, name, age)
#         self.marks = marks
#         print('Initialized Student:{}'.format(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print('Marks: "{:d}"'.format(self.marks))
#
# class Headmaster(SchoolMember):
#     def __init__(self, name, age, marks):
#         SchoolMember.__init__(self,name, age)
#         self.marks = marks
#         print('Initialized Student:{}'.format(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print('Marks: "{:d}"'.format(self.marks))
#
# t = Teacher('Mrs. Shrividya', 40, 30000)
# s = Student('Swaroop', 25, 75)
# h = Headmaster('Dr John', 26, 90)
#
# print()
#
# members = [t,s,h]
# for member in members:
#     member.tell()
#








