def add_student(records):
    name = input("Enter Student's Name: ")
    roll_no = int(input("Enter Roll no.: "))
    if roll_no in records:
        print("Student already exists.\n")
        return
    
    marks = []
    subjects = ["English", "Math", "Computer"]

    for subject in subjects:
        while True:
            try:
                oneSubjectMarks = int(input(f"Enter {subject} marks (0-100): "))
                if 0 <= oneSubjectMarks <= 100:
                    marks.append(oneSubjectMarks)
                    break
                else:
                    print("Marks must be between 0 to 100. Try Again!\n")
            except ValueError:
                print("Invalid input. Please enter a number.")

    records[roll_no] = {"Name" : name, "Roll no." : roll_no, "marks": marks}
    print("Student Added Successfullly!\n")

def view_gradebook(records):
    if not records:
        print("No Students Enrolled Yet!\n")
        return
    print("---- Gradebook ----")
    for roll_no , data in records.items():
        avg = sum(data['marks']) / len(data['marks'])
        grade = (
            "A" if avg >= 90 else
            "B" if avg >= 80 else
            "C" if avg >= 70 else
            "D" if avg >= 60 else
            "F"
        )
        print(f"""
Roll no.   : {roll_no}
Name       : {data["Name"]} 
Average    : {avg:.2f}
Grade      : {grade}
          """)
    
def main():
    records = {}
    print("Pakistan Students Report Card")

    while True:
        print("1. Add Student")
        print("2. View Gradebook")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student(records)
        elif choice == "2":
            view_gradebook(records)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()