class Phone:

   def Display(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)

class Samsung(Phone):

    def Show(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)

class Motorla(Samsung):

    def ShowUp(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)


a = Motorla()
a.Display("Latif", 200)
a.Show("Lukman", 300)
a.ShowUp("Kumar", 300)






