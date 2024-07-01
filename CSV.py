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

    print(f"Successfully wrote {num_students} records to grades.csv")

def read_grades_from_csv():
    # Open the grades.csv file in read mode with newline=''
    with open('grades.csv', mode='r', newline='') as file:
        reader = csv.reader(file)

        # Read and display header row
        header = next(reader)
        print(f"{header[0]:<15} {header[1]:<15} {header[2]:<8} {header[3]:<8} {header[4]:<8}")

        # Read and display each student's data
        for row in reader:
            first_name, last_name, exam1, exam2, exam3 = row
            print(f"{first_name:<15} {last_name:<15} {exam1:<8} {exam2:<8} {exam3:<8}")

if __name__ == "__main__":
    num_students = int(input("Enter number of students: "))
    write_grades_to_csv(num_students)
    read_grades_from_csv()
