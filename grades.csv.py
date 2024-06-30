import csv

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
    read_grades_from_csv()
