import pymysql

# Connect to the database
conn = pymysql.connect(
    host="manchinti-database.cqrpakzfgqej.ap-southeast-2.rds.amazonaws.com",
    user="admin",
    password="12345678",
    db="pavan"
)

# Create a cursor object
cursor = conn.cursor()

# Create a table for students1
table_create_query = '''
    CREATE TABLE students1 (
        id float NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        age INT NOT NULL,
        grade DECIMAL(3,2) NOT NULL,
        PRIMARY KEY (id)
    )
'''
cursor.execute(table_create_query)

# Insert data for three students1
student_data = [
    ('John', 18, 3.5),
    ('Sarah', 20, 4.0),
    ('David', 19, 3.8)
]

insert_query = "INSERT INTO students1 (name, age, grade) VALUES (%s, %s, %s)"

for data in student_data:
    cursor.execute(insert_query, data)

# Commit changes to the database
conn.commit()

# Close the database connection
conn.close()
