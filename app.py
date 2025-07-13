from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = "clave_secreta"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')    

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    # Validar si las contraseñas coinciden
    if password != confirm_password:
        flash('Las contraseñas no coinciden')
        return redirect(url_for('home'))

    # Verificar si el usuario ya existe
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        flash('El nombre de usuario ya está en uso')
        return redirect(url_for('home'))

    # Crear nuevo usuario
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    flash('Usuario registrado con éxito')
    return redirect(url_for('home'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()  # si usas email, cambia esto

    if user and check_password_hash(user.password, password):
        flash('Inicio de sesión exitoso')
        return redirect(url_for('home'))
    else:
        flash('Usuario o contraseña incorrectos')
        return redirect(url_for('home'))
    
if __name__ == '__main__':
    app.run(debug=True)