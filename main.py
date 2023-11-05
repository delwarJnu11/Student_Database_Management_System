import pymysql

DB_NAME = 'SCHOOL'

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password='@delwar11@',
    database= DB_NAME
)

cursor = connection.cursor()

def create_table(table_name):
    query = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    ID INT(5) PRIMARY KEY AUTO_INCREMENT,
                    NAME VARCHAR(50) NOT NULL,
                    AGE INT(4) NOT NULL,
                    GPA FLOAT(3,2) NOT NULL
                ) AUTO_INCREMENT = 100;
            """
    cursor.execute(query)

def add_student(table_name, name,age,gpa):
    query = f"""
                INSERT INTO {table_name} (name, age,gpa)
                VALUES (%s, %s, %s)
            """
    cursor.execute(query, (name,age,gpa))
    connection.commit()

def view_all_student(table_name):
    query = f"""
                SELECT *
                FROM {table_name}
            """
    cursor.execute(query)

    students = cursor.fetchall()
    print('Id - Name - Age - GPA')
    for student in students:
        id, name,age,gpa = student
        print(id, name, age, gpa)
    print("")

def update_student_grade(table_name,student_id, new_info):
    #UPDATE STUDENT GPA
    update_query = f"""
                        UPDATE {table_name}
                        SET gpa = %s
                        WHERE ID = %s
                    """
    cursor.execute(update_query,(new_info, student_id))
    connection.commit()

def age_increment(table_name, student_id, new_age):
    query = f"""
                SELECT AGE
                FROM {table_name}
                WHERE ID = %s
            """
    cursor.execute(query,student_id)
    student = cursor.fetchone()
    updated_age = student[0] + new_age

    update_query = f"""
                        UPDATE {table_name}
                        SET age = %s
                        WHERE ID = %s
                    """
    cursor.execute(update_query,(updated_age, student_id))
    connection.commit()

while True:

    print("""
        1. Create Table
        2. Add Student
        3. Veiw All Student
        4. Update Student Info
        5. Sudent Age Increment
        6. Exit

""")
    
    option = int(input('Enter your Choice: '))
    
    if option == 1:
        #create table
        table_name = input('Enter Table Name: ')
        create_table(table_name)
        print(f'{table_name} Table created successfully done!')
    elif option == 2:
        # add Student into table
        table_name = input('Enter Table Name: ')
        name = input('Enter Student Name: ')
        age = int(input('Enter student age: '))
        gpa = float(input('Enter Student GPA: '))
        add_student(table_name,name,age,gpa)
        print('Student added successfully done!')
    elif option == 3:
        # view all data
        table_name = input('Enter Table Name: ')
        view_all_student(table_name)
    elif option == 4:
        #update Student data
        table_name = input('Enter Table Name: ')
        student_id = int(input('Enter student ID: '))
        gpa = float(input('Enter Student GPA: '))
        update_student_grade(table_name,student_id,gpa)
        print('student GPA Updated!!')
    elif option == 5:
        #Age increment 
        table_name = input('Enter Table Name: ')
        student_id = int(input('Enter student ID: '))
        age = int(input('Enter student increment age: '))
        age_increment(table_name, student_id,age)
        print('Age increment successfully done!')
    elif option == 6:
        break
    else:
        print('please provide valid option')