from functools import wraps
from flask import Flask, request, jsonify, render_template, redirect, session, url_for

app = Flask(__name__)
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_email' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # lógica para verificar login
        email = request.form['email']
        contraseña = request.form['password']

        # Aquí deberías buscar el usuario en la base de datos
        # y verificar la contraseña, por ahora lo simulo:
        if email == "admin@copa.com" and contraseña == "1234":
            session['user_email'] = email
            session['user_role'] = 'admin'
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Datos incorrectos")
    
    return render_template('login.html')

@app.route('/')
def index():
    deportes = [
        {"id": 1, "name": "Futbol", "image": "#"},
        {"id": 2, "name": "Basquet", "image": "#"},
        {"id": 3, "name": "Voley", "image": "#"}
    ]
    data = {
        "title": "Bienvenido a la aplicacion de la Copa!",
        "description": "Esta es una aplicacion de ejemplo para la Copa Renault.",
        "sports": deportes,
        "number_of_sports": len(deportes)
    }
    return render_template('index.html', data=data, deportes=deportes)

@app.route('/pedro')
@login_required
def pedro():
    data = {
        "title": "Pedro"
    }
    return render_template('pedro.html', data=data)
@app.route('/cantina')
# @login_required
def cantina():
    return render_template('cantina.html')

@app.route('/sponsors')
# @login_required
def sponsors():
    return render_template('sponsors.html')

@app.route('/fixtures')
# @login_required
def fixtures():
    return render_template('fixtures.html')

@app.route('/futbol')
# @login_required
def futbol():
    return render_template('./deportes/futbol.html')

@app.route('/basquet')
# @login_required
def basquet():
    return render_template('./deportes/basquet.html')

@app.route('/voley')
# @login_required
def voley():
    return render_template('./deportes/voley.html')


if __name__ == '__main__':
    app.run(debug=True)

