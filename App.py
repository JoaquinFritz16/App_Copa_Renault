from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/pedro')
def pedro():
    data = {
        "title": "Pedro"
    }
    return render_template('pedro.html', data=data)
if __name__ == '__main__':
    app.run(debug=True)
