class Human:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

    def __str__(self):
        return f"Class Name: {self.__class__}, Name Human: {self.Name}, Age Human: {self.Age}"

    def __repr__(self):
        return f"{self.__class__}, {self.Name}, {self.Age}"

    def show_name(self):
        print(self.Name)


class Gender(Human):
    def __init__(self, Name, Age, Gender):
        super().__init__(Name, Age)
        self.Gender = Gender

    def __eq__(self, other):
        if self.Gender == other.Gender:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.Gender != other.Gender:
            return True
        else:
            return False


class Student(Gender):
    def __init__(self, Name, Age, Gender, StudentId):
            super().__init__(Name, Age, Gender)
            self.StudentId = StudentId


m1 = Student("Mikle", 20, "Man", 1)
m2 = Student("Jeny", 30, "Woman", 2)

if m1 == m2:
    print("Гендеры равны")
elif m1 != m2:
    print("Гендеры не равны")

