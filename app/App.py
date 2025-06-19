from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
@app.route('/')
def index():
    deportes = [
        {"id": 1, "name": "Fútbol"},
        {"id": 2, "name": "Basket"},
        {"id": 3, "name": "Voley"}
    ]
    data = {
        "title": "Bienvenido a la aplicacion de la Copa!",
        "description": "Esta es una aplicacion de ejemplo para la Copa del Mundo.",
        "sports": deportes,
        "number_of_sports": len(deportes)
    }
    return render_template('index.html', data=data, deportes=deportes)

@app.route('/pedro')
def pedro():
    data = {
        "title": "Pedro"
    }
    return render_template('pedro.html', data=data)
if __name__ == '__main__':
    app.run(debug=True)
