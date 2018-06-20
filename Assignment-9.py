#Question-1
class circle:
    def __init__ (self,radius):
         self.radius=radius

    def area(self):
        self.area=(3.14*self.radius*self.radius)
        print("the area of circle is:",str (self.area))

    def circumference(self):
         self.circumference= (2*3.14*self.radius)
         print("the circumference is: ", str (self.circumference))

r=int(input("enter any radius: "))
obj1=circle(r)
obj1.area()
obj1.circumference()
print("\n")


#Question-2
class Student:
    def __init__(self, roll, name):
        self.name = name
        self.roll = roll

    def show(self):
        print(self.name, self.roll)


roll = int(input("enter roll no: "))
name = input("enter name: ")
s1 = Student(roll, name)
s1.show()


#Question-3
class Temperature:
    def __init__(self, celcius, Fahrenheit):
        self.Fahrenheit = Fahrenheit
        self.celsius = celcius

    def getFahrenheit(self):
        print("Fahrenheit is", (1.8 * self.celsius) + 32)

    def getcelsius(self):
        print("celsius", (self.Fahrenheit - 32) * 0.55)


Fahrenheit = float(input("enter Fahrenheit"))
celsius = float(input("enter celsius"))
t = Temperature(celsius, Fahrenheit)
t.getFahrenheit()
t.getcelsius()


#Question-4
class moviedetails:
    def __init__(self, moviename, artistname, rating, year):
        self.moviename = moviename
        self.artistname = artistname
        self.year = year
        self.rating = rating

    def getdisplay(self):
        print(self.moviename, self.artistname, self.year, self.rating)

    def update(self, moviename, artistname, rating, year):
        self.moviename = moviename
        self.artistname = artistname
        self.year = year
        self.rating = rating


c = moviedetails("Gold","Akshay", 2018, 5)
c.getdisplay()
c.update("Housefull 4", "Akshay", 2018, 7)
c.getdisplay()


#Question-5
class expenditure:
    def __init__(self, expenditure, saving):
        self.expenditure = expenditure
        self.saving = saving

    def getdisplay(self):
        print("expend is", self.expenditure, "saving is", self.saving)

    def getcalculation(self):
        print("total salary=", self.expenditure + self.saving)


c = expenditure(40000, 50000)
c.getdisplay()
c.getcalculation()


