class Person:
    def __init__(self, pre, mid, fin, std):
        self.__std = std
        self.__pre = pre
        self.__mid = mid
        self.__fin = fin

    def Average(self):
        return (self.__pre + self.__mid + self.__fin) / 3

    def display(self):
        print("Student name:", self.__std)
        print("Prelim:", self.__pre)
        print("Midterm:", self.__mid)
        print("Finals: ", self.__fin)
        print("Average:", self.Average())
        print(" ")

class std_1(Person):
    pass
class std_2(Person):
    pass
class std_3(Person):
    pass

std_1 = Person(87, 90, 96, "student_1")
std_1.display()

std_2 = Person(97, 98, 97, "student_2")
std_2.display()

std_3 = Person(75, 82, 76, "student_3")
std_3.display()



