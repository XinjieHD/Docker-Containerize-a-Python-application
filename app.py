from flask import Flask
import json

app = Flask(__name__)

# Sample student data
students = [
    {"id": 1, "name": "Alice", "term": "Spring 2023"},
    {"id": 2, "name": "Bob", "term": "Fall 2022"},
]

@app.route("/")
def hello():
    return json.dumps(students)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
