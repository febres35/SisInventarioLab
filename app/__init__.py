from flask import Flask

from flask_bootstrap import Bootstrap

from flask_wtf.csrf import CSRFProtect

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # instancia de flask

db = SQLAlchemy()
bootstrap = Bootstrap() # instancia de bootstrap
csrf = CSRFProtect()

#se procede a crear la relacion entre las urls y el servidor

from .views import page
from .init_db import init_DB
#se coloca .views porque se desea importar una funcion o una instancia de un archivo.

from .models import User

def create_app(config):

	app.config.from_object(config) # se le indica al servidores que va a trabajar con objetos de configuraciones
	# app.config --> configurar el servidor
	# from_object --> indica que la configuracion del servidor vendra dada por una clase
	
	csrf.init_app(app)
	bootstrap.init_app(app) # implementacion de bootstrap en el servidor
	bootstrap.BOOTSTRAP_SERVE_LOCAL = True

	with app.app_context():
		db.init_app(app)
		init_DB()

		db.create_all()



	#Le indicamos al servidor que utilice dichas rutas
	app.register_blueprint(page)
	return app