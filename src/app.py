from flask import Flask
from flask import Flask, jsonify
from flask import request



app = Flask(__name__)

todos =  [{ "label": "My first task", "done": False },]

@app.route('/todos', methods=['GET'])
def hello_world():
 return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    try:
        todos.pop(position)
    except IndexError:
        return jsonify({"error": "Position out of range"}), 404
    return jsonify(todos)










if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

  