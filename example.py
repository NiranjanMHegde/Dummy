# class Animal: 
#     def speak(self):
#         print("Animal speaks")

# class dog(Animal):
#         def speak(self):
#             print("Dog barks")
        
# a=Animal()
# b=dog()
# a.speak()
# b.speak()

#Second Question

# class Shape:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height

#     def area(self):
#          return 0
    
# class Rectangle(Shape):
#      def area(self):
#           return (self.width * self.height)
     
# r1=Rectangle(3,4)
# print(r1.area())


#Question 3

class Vehicle:
    def start_engine(self):
        print("Engine Started")

class car(Vehicle):
    def start_engine(self):
        print("car engine started")
    
class motorcycle(Vehicle):
    def start_engine(self):
        print("motorcycle engine started")

a=Vehicle()
b=car()
c=motorcycle()
a.start_engine()
b.start_engine()
c.start_engine()

    
#Good morning