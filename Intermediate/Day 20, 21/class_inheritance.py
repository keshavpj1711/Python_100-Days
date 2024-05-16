# Consider we have these two classes

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


# To inherit Animal class in Fish() we have to do the following
class Fish(Animal):  # First, we have to do Fish(Animal)
    def __init__(self):
        super().__init__()  # Second, we do this to inherit all the methods from the Animal class
        # So all in all The call to super() in the initializer is recommended, but not strictly required.

    # Now let say we need to modify the breathe function, i.e., we need to add something more so
    def breathe(self):
        super().breathe()
        print("doing it underwater")

    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()