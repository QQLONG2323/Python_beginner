from Lesson13_tools import Person

p1 = Person("余友中", 32, True)
print(p1)
print(p1.name)
print(p1.age)
print(p1.sex)
#help(p1)
#print(p1.__dict__)
p1.age = 40
print(p1.age)


p2 = Person("友中余", 18, False)
print(p2)
print(p2.name)
print(p2.age)
print(p2.sex)