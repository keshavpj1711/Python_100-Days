# Creating a class
class Student:
    pass


# Creating an object using our created class
student1 = Student()
# Adding attribute for an object
student1.roll = "22EE30015"
student1.name = "Keshav"
print(student1.roll)
print(student1.name)


# Creating a second object
student2 = Student()
# Adding attributes
student2.id = 2
student2.name = "Rahul"
#  That's exactly the power of classes and objects in Python.
#  You can create different attributes for different objects even though they are instances of the same class.


# Using Class Constructors
class User:

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.user_name = username
        # Setting up default attributes
        self.follower = 0
        self.following = 0
        print("This prints everytime the initialization of a new object occurs")

    # Adding methods to a class
    def follow(self, user):
        user.follower += 1
        self.following += 1


# Creating an object whose values are being passed
user_1 = User("30015", "Keshav")
print(user_1.user_name)


