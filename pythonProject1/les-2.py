class Student:

    def __init__(self,height = 170):
        self.height = height

nick = Student()
Kate = Student(height = 170)
print(nick.height)
print(kate.height)