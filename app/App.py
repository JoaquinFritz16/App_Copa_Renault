from functools import wraps
from flask import Flask, request, jsonify, render_template, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'una_clave_segura_y_larga'
equipos_registrados = []
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

        #simulacion porque no funciona la base de datos
        if email == "admin@copa.com" and contraseña == "1234":
            session['user_email'] = email
            session['user_role'] = 'admin'
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Datos incorrectos")
    
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

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
@login_required
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
@app.route('/registrar_equipo', methods=['GET', 'POST'])
def registrar_equipo():
    if request.method == 'POST':
        nombre_equipo = request.form['nombre']
        deporte = request.form['deporte']

        # Validación simple para evitar duplicados
        for equipo in equipos_registrados:
            if equipo['nombre'] == nombre_equipo and equipo['deporte'] == deporte:
                return render_template('registrar_equipo.html', error="Ese equipo ya está registrado.")

        # Simulamos guardar
        equipos_registrados.append({
            'nombre': nombre_equipo,
            'deporte': deporte
        })

        return redirect(url_for('lista_equipos'))

    return render_template('registrar_equipo.html')
@app.route('/equipos')
def lista_equipos():
    return render_template('equipos.html', equipos=equipos_registrados)


if __name__ == '__main__':
    app.run(debug=True)

