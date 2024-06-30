import csv

def write_grades_to_csv(num_students):
    # Open the grades.csv file in write mode with newline=''
    with open('grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # Input student data and write each student as a record
        for _ in range(num_students):
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

if __name__ == "__main__":
    num_students = int(input("Enter number of students: "))
    write_grades_to_csv(num_students)
    print(f"Successfully wrote {num_students} records to grades.csv")
