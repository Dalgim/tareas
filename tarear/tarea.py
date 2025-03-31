'''
    Se crearan las vistas de las tareas en esta zona, utilizaremos
    blueprint para dar un orden a las vistas, por ello utilizaremos la
    libreria de flask del mismo nombre blueprint
'''

from flask import Blueprint, render_template, request, url_for, redirect, g
# importamos la funcion de autenticacion de login para que no se acceda si no esta logueado
from tarear.auth import login_required
# importamos los modelos de la BD
from .models import task, user
from tarear import db

# creamos una instancia de la libreria blueprint
# url prefix es la url inicial de donde inicia la aplicacion
bp = Blueprint('tarea', __name__, url_prefix='/task')

# podemos usar decoradores con blueprint para la vista de lista de tareas
@bp.route('/GET/tasks')
# indicamos con decoradores que tiene que loguearse para entrar a esta vista
@login_required
# creamos una funcion de retorno de la ruta
def index():
    # recuperamos la lista de tareas
    tareas = task.query.all()
    #return 'Lista de Tareas'
    return render_template('tareas/index.html', tareas = tareas)

# podemos usar decoradores con blueprint para la vista de creacion de una tarea nueva
@bp.route('/POST/tasks', methods = ('GET', 'POST'))
@login_required
# creamos una funcion de retorno de la ruta
def create():
    if request.method == 'POST':
        # obtenemos los datos del formulario en create.html
        title = request.form['title']
        desc = request.form['desc']
        # creamos el objeto para insertar datos en la BD
        tarea_ins = task(g.User.id, title, desc)
        # insertamos los datos del formulario en la BD
        db.session.add(tarea_ins)
        db.session.commit()

        return redirect(url_for('tarea.index'))
    # return 'Crear Tarea'
    return render_template('tareas/create.html')

# obtenermos el listado de ids para poder editar / eliminar
def get_tareas(id):
    tarea = task.query.get_or_404(id)
    return tarea

# podemos usar decoradores con blueprint para la vista de actualizacion de tarea
# pasamos por medio de get el id de la tarea a verificar
@bp.route('/PUT/tasks/<int:id>', methods = ('GET', 'POST'))
@login_required
# creamos una funcion de retorno de la ruta y pasamos el ID de la tarea
def update(id):
    gtarea = get_tareas(id)
    #return 'Actualizar Tarea'
    if request.method == 'POST':
        # pasamos los datos de la base de datos a cada campo del formulario de update.html
        gtarea.title = request.form['title']
        gtarea.desc = request.form['desc']
        gtarea.state = True if request.form.get('state') == 'on' else False
        # damos commit a la actualizacion
        db.session.commit()

        return redirect(url_for('tarea.index'))
    return render_template('tareas/update.html', gtarea = gtarea)

# podemos usar decoradores con blueprint para la vista de eliminiacion de una tarea
@bp.route('/DELETE/task/<int:id>')
@login_required
# creamos una funcion de retorno de la ruta
def delete(id):
    gtarea = get_tareas(id)
    # eliminamos la tarea
    db.session.delete(gtarea)
    db.session.commit()
    # return 'Eliminar Tarea'
    # redireccionamos a la lista de tareas
    return redirect(url_for('tarea.index'))