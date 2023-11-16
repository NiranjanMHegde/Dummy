class Animal:
    def speak(self):
        print("Animal speaks")

class dog(Animal):
        def speak(self):
            print("Dog barks")
        
a=Animal()
b=dog()
a.speak()
b.speak()

