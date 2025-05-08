import mysql.connector



conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="admin@1234",
    database="school"
)
cursor=conn.cursor()
def add_student():
    name=input("Enter Name:")
    age=input("Enter Age:")
    grade=input("Enter Grade:")
    cursor.execute("INSERT INTO students(name,age,grade) VALUES(%s,%s,%s)",(name,age,grade))
    conn.commit()
    print("students added.")
def view_students():
    cursor.execute("SELECT * FROM students")
    for students in cursor.fetchall():
        print(students)
def update_student():
    student_id=input("Enter student ID to update:")
    name = input("Enter Name:")
    age = input("Enter Age:")
    grade = input("Enter Grade:")
    cursor.execute("UPDATE students SET name=%s ,age=%s, grade=%s WHERE id=%s",(name,age,grade,student_id))
    conn.commit()
    print("student updated.")
def delete_student():
    student_id=input("Enter student ID to delete:")
    cursor.execute("DELETE FROM students WHERE id=%s",(student_id,))
    conn.commit()
    print("student Deleted.")
def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1 Add Student")
        print("2 View Student")
        print("3 Update Student")
        print("4 Delete Student")
        print("5 Exit")

        choice=input("Enter choice: ")
        if choice=='1':
            add_student()
        elif choice=='2':
            view_students()
        elif choice=='3':
            update_student()
        elif choice=='4':
            delete_student()
        elif choice=='5':
            break
        else:
            print("Invalid choice")
menu()