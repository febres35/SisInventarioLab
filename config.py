
class Config():
	SECRET_KEY = 'InventarioCasaLAB'
	#se recomienda una llave alfanumerica y compleja

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql://adminLab:Casalab2022@localhost/sisInventarioLab' #conexion a la base de datos
	#<gestorDB>://<user>:<pwd>@<servidor>/<dbname>


config = {
	'development': DevelopmentConfig,
	'default': DevelopmentConfig
}