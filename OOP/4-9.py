class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        first_letter_name = self.name[0]
        last_name = self.surname
        seniority_str = str(self.seniority)
        
        if self.age >= 18:
            return f"{last_name.upper()}{first_letter_name.upper()}{seniority_str.upper()}"
        else:
            return f"{last_name.lower()}{first_letter_name.lower()}{seniority_str.lower()}"

def main():
    employee1 = C("Anna", "May", 17, 7)
    employee2 = C("George", "Brown", 21, 4)

    print(employee1)
    print(employee2)

if __name__ == "__main__":
    main()
