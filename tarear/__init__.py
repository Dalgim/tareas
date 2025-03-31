'''
Archivo de configuraciones básicas
'''
# importamos las librerias
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# creamos una extension de bd de sql alchemy
db = SQLAlchemy()

# podemos crear instancias de la aplicacion 
def create_app():

    #creamos el decorador app
    app = Flask(__name__)

    # configuracion del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = "sqlite:///tareas.db"
    )

    # inicializamos la conexion a BD
    db.init_app(app)

    # registramos los blueprints
    from . import tarea
    app.register_blueprint(tarea.bp)
    from . import auth
    app.register_blueprint(auth.bp)

    # usamos decoradores para definir rutas
    @app.route('/')
    def index():
        # return 'Hola Mundo!!!!'
        # returnamos la pagina index.html de la carpeta templates con render_template
        return render_template('index.html')
    
    # migramos todos los modelos que se creen dentro de la aplicacion
    with app.app_context():
        db.create_all()
    
    return app
