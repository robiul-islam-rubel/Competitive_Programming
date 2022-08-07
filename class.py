class myclass:
    x=5
p=myclass()
print(p.x)


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printname(self):
        print(self.name,self.age)

p = person("Rubel",35)
p.printname()