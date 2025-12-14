# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.skin_colour = "white"

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.skin_colour = "black"
    student2.name = "Olivia"
    student2.age = 21
    student2.skin_colour = "yellow"
    student2.name = "Dawid"
    student2.age = 22
    student2.skin_colour = "green"


    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, {student1.skin_colour}')
    print(f'{student2.name}, {student2.age} years old, {student2.skin_colour}')
    print(f'{student3.name}, {student3.age} years old, {student3.skin_colour}')

if __name__ == "__main__":
    main()