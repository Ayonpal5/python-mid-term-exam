class Student:
    def __init__(self, student_id, name, department):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = True
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.is_enrolled:
            print(f"Error: Student {self.name} (ID: {self.student_id}) is already enrolled.")
        else:
            self.is_enrolled = True
            print(f"Success: Student {self.name} has been successfully enrolled.")

    def drop_student(self):
        if not self.is_enrolled:
            print(f"Error: Student {self.name} (ID: {self.student_id}) is not currently enrolled.")
        else:
            self.is_enrolled = False
            print(f"Success: Student {self.name} has been dropped from enrollment.")

    def view_student_info(self):
        status = "Enrolled" if self.is_enrolled else "Not Enrolled"
        print("-" * 40)
        print(f"Student ID   : {self.student_id}")
        print(f"Name         : {self.name}")
        print(f"Department   : {self.department}")
        print(f"Status       : {status}")
        print("-" * 40)
class StudentDatabase:
    student_list = []  
    @classmethod
    def add_student(cls, student_obj):
        cls.student_list.append(student_obj)
    @classmethod
    def find_student(cls, student_id):
        for student in cls.student_list:
            if student.student_id == student_id:
                return student
        return None
def main_menu():
    Student("101", "Alice Smith", "Computer Science")
    Student("102", "Bob Jones", "Electrical Engineering")

    while True:
        print("\n===== Student Management System =====")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            if not StudentDatabase.student_list:
                print("\nNo students found in the database.")
            else:
                print("\n--- All Students List ---")
                for student in StudentDatabase.student_list:
                    student.view_student_info()

        elif choice == '2':
            s_id = input("Enter Student ID to enroll: ").strip()
            student = StudentDatabase.find_student(s_id)
            if student is None:
                print(f"Error: Student with ID '{s_id}' does not exist in the database.")
            else:
                student.enroll_student()

        elif choice == '3':
            s_id = input("Enter Student ID to drop: ").strip()
            student = StudentDatabase.find_student(s_id)
            if student is None:
                print(f"Error: Student with ID '{s_id}' does not exist in the database.")
            else:
                student.drop_student()

        elif choice == '4':
            print("\nExiting system. Good luck with your exam!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main_menu()
