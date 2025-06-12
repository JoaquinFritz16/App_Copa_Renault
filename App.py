from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/')
def principal():
    return 'Welcome to the Flask App!'
if __name__ == '__main__':
    app.run(debug=True)
