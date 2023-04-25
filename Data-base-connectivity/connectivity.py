from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)

# database connectivity
conn = pymysql.connect(
    host="database-1.ccoklqryoopl.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="123456789",
    db="navadeep"
)

# create services table
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS services (
  id INT(11) NOT NULL AUTO_INCREMENT,
  region VARCHAR(255) NOT NULL,
  tag VARCHAR(255) NOT NULL,
  instance_type VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
)
""")
conn.commit()

# insert sample data to the database table
cursor.execute("INSERT INTO services (region, tag, instance_type) SELECT * FROM (SELECT 'us-west-1', 'ec2', 't2.micro') AS tmp WHERE NOT EXISTS (SELECT id FROM services WHERE region = 'us-west-1' AND tag = 'ec2' AND instance_type = 't2.micro') LIMIT 1;")
cursor.execute("INSERT INTO services (region, tag, instance_type) SELECT * FROM (SELECT 'us-west-2', 's3', 'standard') AS tmp WHERE NOT EXISTS (SELECT id FROM services WHERE region = 'us-west-2' AND tag = 's3' AND instance_type = 'standard') LIMIT 1;")
cursor.execute("INSERT INTO services (region, tag, instance_type) SELECT * FROM (SELECT 'us-east-1', 'rds', 'db.t2.micro') AS tmp WHERE NOT EXISTS (SELECT id FROM services WHERE region = 'us-east-1' AND tag = 'rds' AND instance_type = 'db.t2.micro') LIMIT 1;")
conn.commit()


# route to get all services
@app.route('/services')
def get_services():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM services")
        rows = cursor.fetchall()
        # convert rows to list of dictionaries
        services = []
        for row in rows:
            service = {
                'region': row[1],
                'tag': row[2],
                'instance_type': row[3]
            }
            services.append(service)
        return jsonify(services)
    except Exception as e:
        print(e)
        return jsonify({'error': 'failed to retrieve services'})

# route to get a specific service using request headers
@app.route('/service')
def get_service():
    try:
        tag = request.headers.get('tag')
        if not tag:
            return jsonify({'error': 'TAG not provided in request headers'})
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM services WHERE tag='{tag}'")
        row = cursor.fetchone()
        if row:
            # convert row to dictionary
            service = {
                'region': row[1],
                'tag': row[2],
                'instance_type': row[3]
            }
            return jsonify(service)
        else:
            return jsonify({'error': 'service not found'})
    except Exception as e:
        print(e)
        return jsonify({'error': 'failed to retrieve service'})

# route to get a specific service using route parameter
@app.route('/services/<string:tag>')
def get_service_by_tag(tag):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM services WHERE tag='{tag}'")
        row = cursor.fetchone()
        if row:
            # convert row to dictionary
            service = {
                'region': row[1],
                'tag': row[2],
                'instance_type': row[3]
            }

            return jsonify(service)
        else:
            return jsonify({'error': 'service not found'})
    except Exception as e:
        print(e)
        return jsonify({'error': 'failed to retrieve service'})

# route to create a new service
@app.route('/service', methods=['POST'])
def create_service():
    try:
        # get data from request body
        data = request.json
        region = data['region']
        tag = data['tag']
        instance_type = data['instance_type']
        # insert data into database
        cursor = conn.cursor()
        cursor.execute(f"insert into servises (region, tag, instance_type) values ('{region}', {tag}, {instance_type})")
        conn.commit()
        # return success message
        return jsonify({'message': 'service created successfully'})
    except Exception as e:
        print(e)
        return jsonify({'error': 'failed to create service'})

if __name__ == '__main__':
    app.run(debug=True)