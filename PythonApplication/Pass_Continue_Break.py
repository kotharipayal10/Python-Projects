s = "geeks"
  
# Pass statement 
for i in s: 
    if i == 'k': 
        print('Pass executed') 
        pass
        print("Will this execute ?")
    print(i) 
  
print() 
      
# Continue statement 
for i in s: 
    if i == 'k': 
        print('Continue executed') 
        continue
    print(i)

print("Define a new class")

class Payal:
    pass


# except Exception as e:
#     pass

p = Payal()
p.field1 = 1
print(p.field1)

p1 = Payal()
p1.field2 = 2
p1.field1 = 3
print(p1.field2)
print(p1.field1)
print(p.field1)


class Calculation:
    f1 = 5
    f2 = 6
    field1 = 3

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def sum(self): 
        return self.field1 + self.field2 + Calculation.field1

    def mult(self):
        pass

    def div(self):
        pass

    def subs(self):
        pass

    @staticmethod
    def print(self):
        print(Calculation.f1, Calculation.f2)
        print(self.field1)

c1 = Calculation(1, 2)
print(c1.field1, c1.field2)
print(c1.sum())
print(c1.mult())

print("Class Values : ", Calculation.print(c1))