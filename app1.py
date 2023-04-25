from flask import Flask, jsonify, request

app = Flask(__name__)

data = {
    "students": [
        {
            "id": 1,
            "name": "Alice",
            "age": 20
        },
        {
            "id": 2,
            "name": "Bob",
            "age": 21
        }
    ]
}

# Route to get all students data
@app.route('/students')
def get_students():
    return jsonify(data)

# Route to add a new student
@app.route('/students', methods=['POST'])
def add_student():
    student = request.get_json()
    # Generate new ID
    student_id = max([s['id'] for s in data['students']]) + 1
    student['id'] = student_id
    # Add student to data
    data['students'].append(student)
    return jsonify({'message': 'Student added successfully'})

# Route to delete a student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    # Check if student exists
    student = next((s for s in data['students'] if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'})
    # Remove student from data
    data['students'].remove(student)
    return jsonify({'message': 'Student deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True,port=120)