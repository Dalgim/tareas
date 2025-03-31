'''
este sera el documento principal de ejecucion de la app
'''

# importamos las configuraciones del archivo __init__.py
from tarear import create_app

# con esto podemos correr directamente el servicio sin necesidad de una instancia
if __name__ == '__main__':
    app = create_app()
    app.run()