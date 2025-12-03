import csv



def assign_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


input_file = 'students.csv'
output_file = 'graded_students.csv'

students_data = []

try:
    with open(input_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            name = row['Name']
            marks = int(row['Marks'])
            grade = assign_grade(marks)
            
            students_data.append({'Name': name, 'Marks': marks, 'Grade': grade})

    
    with open(output_file, mode='w', newline='') as file:
        fieldnames = ['Name', 'Marks', 'Grade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students_data)

    print("Grading completed successfully! Check 'graded_students.csv'.")
    for student in students_data:
        print(f"{student['Name']} - {student['Marks']} - Grade: {student['Grade']}")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except Exception as e:
    print("An error occurred:", e)
