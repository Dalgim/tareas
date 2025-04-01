Para ejecutar el proyecto, se tiene que tener instalado python. Importante que durante la instalacion se agregue la opcion de
agregar las variables en el path y quitar la seleccion de la opcion de tamañano maximo permitido al final de la instalacion.

1. Crear una carpeta donde se alojara el proyecto
2. ejecutar git clone https://github.com/Dalgim/tareas.git
3. abrir una terminal o en vscode y ejecutar el siguiente comando "python -m venv env-tareas" (windows) o "python3 -m venv env-tareas" (linux)
4. ejecutar el entorno virtual con "env-tareas/Scripts/activate" (windows) ó "env-tareas/bin/activate" (linux)
5. Verificamos con el comando "pip list" que aplicaciones tenemos en el entorno virtual
6. en caso de ser necesario instalar la ultima version de pip con "python.exe -m pip install --upgrade pip"
7. luego instalar flask por medio del comando "pip install flask"
8. adicional instalar Flask-SQLAlchemy con el comando "pip install Flask-SQLAlchemy"
9. una vez instalados los paquetes ejecutar el proyecto con "python run.py" (windows) o "python3 run.py" (linux)
