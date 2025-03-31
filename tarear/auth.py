'''
    Modulo que contendra toda la parte de autenticación de usuarios para el login
    render_template nos permite cargar archivos html dentro de las rutas
'''

# Importamos librerias mara llamadas request, redirect para redireccion a vistas,
# flash para manejo de errores, session para uso de sesion al loguearnos
# g para guardar valores para luego utilizarlo en cuaquier parte de la aplicacion
from flask import (
    Blueprint, render_template, request, url_for, redirect, flash,
    session, g
)
# importamos la libreria werkzeug que trabaja con seguridad
from werkzeug.security import generate_password_hash, check_password_hash
import functools

# importamos los modelos de la BD y la instancia
from .models import user
from tarear import db

# creamos una instancia de la libreria blueprint
# url prefix es la url inicial de donde puede iniciar el modulo
bp = Blueprint('auth', __name__, url_prefix='/auth')

# podemos usar decoradores con blueprint para la vista de registro de usuarios
@bp.route('/register', methods = ('GET', 'POST'))
# creamos una funcion para la vista de registro de usuario de la ruta
def register():
    if request.method == 'POST':
        # obtenemos los datos del formulario de register
        username = request.form['username']
        password = request.form['password']
        
        #pasamos los datos para insertarlos, encriptamos el password en la BD
        User = user(username, generate_password_hash(password))

        # creamos una variable para manejo de errores
        error = None

        # buscamos en la base de datos
        user_name = user.query.filter_by(username = username).first()

        # Si no existe el nombre de usuario, entonces agrega el registro
        if user_name == None:
            # insertamos los datos a la BD
            db.session.add(User)
            db.session.commit()
            # nos redirige a la vista de login
            return redirect(url_for('auth.login'))
        else:
            # si existe entonces manejamos errores en este parte
            error = f'El usuario {username} ya esta registrado'
        
        # utilizamos esta libreria para dar formato a los manejos de errores
        flash(error)

    # return 'Registra Usuarios'
    return render_template('auth/register.html')

# podemos usar decoradores con blueprint para la creacion de una tarea nueva
@bp.route('/login' , methods = ('GET', 'POST'))
# creamos una funcion de retorno de la ruta
def login():

    if request.method == 'POST':
        # obtenemos los datos del formulario de register
        username = request.form['username']
        password = request.form['password']

        # creamos una variable para manejo de errores
        error = None

        # buscamos en la base de datos
        User = user.query.filter_by(username = username).first()

        # validamos que los datos sean correctos con lo que hay en BD
        if User == None:
            error = 'Nombre de usuario Incorrecto'
        elif not check_password_hash(User.password, password):
            error = 'Contraseña Incorrecta'
        
        # Iniciamos sesion

        # Si no existe algun error, entonces iniciamos sesion
        if error is None:
            # iniciamos las variables de sesion, limpiamos las variables si es que
            # ya existen
            session.clear()
            # iniciamos las variables de la sesion
            session['user_id'] = User.id
            # mandamos a la pagina de index
            return redirect(url_for('tarea.index'))
        
        # utilizamos esta libreria para dar formato a los manejos de errores
        flash(error)

    # return 'Iniciar Sesion'
    return render_template('auth/login.html')

# registramos la sesion con blueprint para usarla en cualquier parte del sitio
@bp.before_app_request
# creamos una funcion que permita mantener la sesion siempre en cualquier parte del sitio
def load_logged_in_user():
    # obtenemos el id del usuario que inicio sesion
    user_id = session.get('user_id')

    # alamcenamos y obtenemos un dato de la sesion, usando la libreria de g
    if user_id is None:
        g.User = None
    else:
        g.User = user.query.get_or_404(user_id)

# creamos una vista para cerrar sesion
# definimos la ruta con blueprint
@bp.route('/logout')
def logout():
    # limpíamos la sesion
    session.clear()
    # redirigimos a la pagina de inicio de la aplicacion con return
    return redirect(url_for('index'))


# definimos una funcion para solicitar siempre un logueo requerido
def login_required(view):
    #usamos un decorador de functools
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.User is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view