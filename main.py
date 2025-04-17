class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("----------------------")


students = []

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Enter student details :")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = int(input("Enter marks: "))
        s = Student(name, age, marks)
        students.append(s)
    elif choice == 2:
        print("\n--- Student List ---")
        for stu in students:
            stu.display()
    elif choice == 3:
        print("Exited")
        break
    else:
        print("Invalid choice.")
