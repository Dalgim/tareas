'''
este modulo contendra todas las conexiones a base de datos
'''
# importamos la instancia de conexion de tarear
from tarear import db
from datetime import datetime, date

# creamos clases para los objetos de la BD es decir las tablas a crear
# tabla para usuarios y manejo del login
class user(db.Model):
    # creamos los campos de la bd
    # creamos un id de tipo entero que sea llave primaria
    id = db.Column(db.Integer, primary_key = True)
    # creamos un username que sea de tipo varchar de tamaño 20 que sea valores unicos
    # y no permita valores nulos
    username = db.Column(db.String(20), unique = True, nullable = False)
    # Creamos un campo para password de tipo Text para longitudes largas y que no permita
    # nulos
    password = db.Column(db.Text, nullable = False)

    # creamos un constructor
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    # obtenemos el dato de representacion del usuario
    def __repr__(self):
        return f'<User: {self.username} >'

# creamos clases para los objetos de la BD es decir las tablas a crear
# tabla para el registro de tareas
class task(db.Model):
    # creamos los campos de la bd
    # creamos un id de tipo entero que sea llave primaria
    id = db.Column(db.Integer, primary_key = True)
    # creamos una llave foranea con la tabla user
    created_by = db.Column(db.Integer, db.ForeignKey(user.id), nullable = False)
    # creamos un titulo de la tarea que sea de tipo varchar de tamaño 100 que sea valores unicos
    # y no permita valores nulos
    title = db.Column(db.String(100), nullable = False)
    # Creamos un campo para descripcion de tipo Text para longitudes largas y que no permita
    # nulos
    desc = db.Column(db.Text)
     # creamos un campo para determinar la fecha de creacion
    created_at = db.Column(db.DateTime, default=datetime.now())
    # creamos un campo de estado si esta completa o no la tarea, de tipo boleano con valor
    # por defecto False (incompleta)
    state = db.Column(db.Boolean, default = False)
    # creamos un campo para determinar si tiene fecha de actualizacion
    #updated_at = db.Column(db.DateTime default=datetime.now())

    # creamos un constructor
    def __init__(self, created_by, title, desc, created_at = datetime.now(), state = False):
        self.created_by = created_by
        self.title = title
        self.desc = desc
        self.created_at = created_at
        self.state = state
        #self.updated_at = updated_at
    
    # obtenemos el dato de representacion del usuario
    def __repr__(self):
        return f'<Task: {self.title} >'