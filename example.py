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

class Shape:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
         return 0
    
class Rectangle(Shape):
     def area(self):
          return (self.width * self.height)
     
r1=Rectangle(3,4)
print(r1.area())

    
          