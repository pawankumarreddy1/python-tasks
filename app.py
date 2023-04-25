# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/data1', methods=['GET'])
# def get_data():
#     data = {"sno": 1 ,"first_name": "Pavan kumar reddy ", "last_name": "manchinti"}
#     return jsonify(data)
# @app.route('/data2', methods=['post'])
# def get_data2():
#     data2 = {"sno": 2 ,"first_name": "Pavan kumar reddy ", "last_name": "manchinti"}
#     return jsonify(data)
# @app.route ('/data3', methods=['post'])
# # def get_data():
# #     data = {"sno":3 ,"first_name ":"ganesh" , "last_name" :"reddy"}
# #     return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=3000)


from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data1', methods=['GET'])
def get_data():
    data = {"sno": 1 ,"first_name": "Pavan kumar reddy ", "last_name": "manchinti"}
    return jsonify(data)

@app.route('/data2', methods=['post'])
def get_data2():
    data2 = {"sno": 2 ,"first_name": "Pavan ", "last_name": "manchinti"}
    return jsonify(data2)

@app.route ('/data3', methods=['post'])
def get_data3():
    data = {"sno":3 ,"first_name ":"ganesh" , "last_name" :"reddy"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
# Pavan1234