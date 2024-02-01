import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('marks.db')
cursor = conn.cursor()

# Create a table for storing marks
cursor.execute('''CREATE TABLE IF NOT EXISTS marks
                  (student_id INTEGER PRIMARY KEY, roll_no TEXT, subject TEXT, mark REAL)''')


def insert_marks(roll_no, subject, mark):
    # Insert marks into the table
    cursor.execute('INSERT INTO marks (roll_no, subject, mark) VALUES (?, ?, ?)', (roll_no, subject, mark))
    conn.commit()


def get_marks(roll_no):
    # Retrieve marks for a specific roll number from the database
    cursor.execute('SELECT subject, mark FROM marks WHERE roll_no = ?', (roll_no,))
    marks = cursor.fetchall()
    return marks


def compare_marks(roll_no1, roll_no2):
    # Get marks for the first student
    marks1 = get_marks(roll_no1)

    # Get marks for the second student
    marks2 = get_marks(roll_no2)

    # Display the marks for both students
    print(f"\nMarks for Student {roll_no1}:")
    display_marks(marks1)

    print(f"\nMarks for Student {roll_no2}:")
    display_marks(marks2)

    # Compare total marks
    total_marks1 = sum(mark for _, mark in marks1)
    total_marks2 = sum(mark for _, mark in marks2)

    # Display the comparison
    print("\nComparison:")
    if total_marks1 > total_marks2:
        print(f"Student {roll_no1} has scored higher marks than Student {roll_no2}.")
    elif total_marks1 < total_marks2:
        print(f"Student {roll_no2} has scored higher marks than Student {roll_no1}.")
    else:
        print(f"Both Student {roll_no1} and Student {roll_no2} have scored the same marks.")

    # Visualize the marks using a graph
    subjects1, marks1 = zip(*marks1)
    subjects2, marks2 = zip(*marks2)

    plt.figure(figsize=(10, 6))
    plt.bar(subjects1, marks1, label=f"Student {roll_no1}")
    plt.bar(subjects2, marks2, label=f"Student {roll_no2}")
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.title("Comparison of Marks")
    plt.legend()
    plt.show()


def display_marks(marks):
    print("Subject\t\tMark")
    print("--------------------")
    for row in marks:
        subject, mark = row
        print(f"{subject}\t\t{mark}")
    print("--------------------")


# Get the number of students
num_students = int(input("Enter the number of students: "))

# Get the marks for each student and store them in the database
for i in range(1, num_students + 1):
    print(f"\nEnter marks for Student {i}:")
    roll_no = input("Enter the roll number: ")
    num_subjects = int(input("Enter the number of subjects: "))
    for j in range(1, num_subjects + 1):
        subject = input(f"Enter the name of subject {j}: ")
        mark = float(input(f"Enter the mark for {subject}: "))
        insert_marks(roll_no, subject, mark)

# Compare marks for two students
roll_no1 = input("\nEnter the roll number of Student 1: ")
roll_no2 = input("Enter the roll number of Student 2: ")
compare_marks(roll_no1, roll_no2)

# Close the database connection
conn.close()
