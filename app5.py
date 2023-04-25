from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)

# database connection
conn = pymysql.connect(
    host="manchinti-database.cqrpakzfgqej.ap-southeast-2.rds.amazonaws.com",
    user="admin",
    password="12345678",
    db="pavan"
)

# route to get all students
@app.route('/students')
def get_students():
    try:
        cursor = conn.cursor()
        cursor.execute("select * from students")
        rows = cursor.fetchall()
        # convert rows to list of dictionaries
        students = []
        for row in rows:
            student = {
                'id': row[0],
                'name': row[1],
                'age': row[2],
                'grade': row[3]
            }
            students.append(student)
        return jsonify(students)
    except Exception as e:
        print(e)
        return jsonify({'error': 'failed to retrieve students'})

# route to get a specific student using request headers
@app.route('/student')
def get_student():
    try:
        id = request.headers.get('id')
        if not id:
            return jsonify({'error': 'ID not provided in request headers'})
        cursor = conn.cursor()
        cursor.execute(f"select * from students where id={id}")
        row = cursor.fetchone()
        if row:
            # convert row to dictionary
            student = {
                'id': row[0],
                'name': row[1],
                'age': row[2],
                'grade': row[3]
            }
            return jsonify(student)
        else:
            return jsonify({'error': 'student not found'})
    except Exception as e:
        print(e)
        return jsonify({'error': 'failed to retrieve student'})

# route to get a specific student using route parameter
@app.route('/students/<int:id>')
def get_student_by_id(id):
    try:
        cursor = conn.cursor()
        cursor.execute(f"select * from students where id={id}")
        row = cursor.fetchone()
        if row:
            # convert row to dictionary
            student = {
                'id': row[0],
                'name': row[1],
                'age': row[2],
                'grade': row[3]
            }
            return jsonify(student)
        else:
            return jsonify({'error': 'student not found'})
    except Exception as e:
        print(e)
        return jsonify({'error': 'failed to retrieve student'})

# route to create a new student
@app.route('/student', methods=['POST'])
def create_student():
    try:
        # get data from request body
        data = request.json
        name = data['name']
        age = data['age']
        grade = data['grade']
        # insert data into database
        cursor = conn.cursor()
        cursor.execute(f"insert into students (name, age, grade) values ('{name}', {age}, {grade})")
        conn.commit()
        # return success message
        return jsonify({'message': 'student created successfully'})
    except Exception as e:
        print(e)
        return jsonify({'error': 'failed to create student'})

if __name__ == '__main__':
    app.run(debug=True)

