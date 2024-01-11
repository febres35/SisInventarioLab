from . import db
import datetime
from sqlalchemy import and_, func, select, join, or_
class User(db.Model):

	__tablename__ = 'users' # este atributo le da nombre a la tabla, si no se coloca toma el nombre de la clase

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True, nullable=False)
	password =	db.Column(db.String(150), nullable=False)
	created_at = db.Column(db.DateTime(), default = datetime.datetime.now())

	def __str__(self):
		return self.username

	@classmethod
	def create_element(cls, username, password):
		user = User(username=username, password=password)

		db.session.add(user) #agrega registro
		db.session.commit()	#actualiza los cambios

		return user


class Unit(db.Model):
	__tablename__= 'units'

	id = db.Column(db.Integer, primary_key=True)
	unitName = db.Column(db.String(25), unique=True, nullable=False)
	article = db.relationship('Article', backref='unit', lazy=True)
	#un tipo de articulo representa a un conjunto de articulos.

	def __str__(self):
		return self.unidad

	@classmethod
	def create_elemet(cls, unitName):
		unit = Unit(unitName = unitName)

		db.session.add(unit)
		db.session.commit()

class Article(db.Model):
	__tablename__ = 'articles'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(25), unique=True, nullable=False)
	description = db.Column(db.Text, nullable=True)
	#se declara que cada registro de Articulo contendra un tipo de dato
	unit_id = db.Column(db.Integer, db.ForeignKey('units.id'))

	#un articulo representa tiene un stock en el inventario.
	stock = db.relationship('Stock', backref='article', lazy=True)
	consumo_insumos = db.relationship('Consumo', backref='article', lazy=True)
	carga_insumos = db.relationship('Carga', backref='article', lazy=True)
	diferencias_insumos = db.relationship('Diferencia', backref='article', lazy=True)

	def __str__(self):
		return self.name

	@classmethod
	def create_elemet(cls, name, description, unit_id):
		article = Article(name = name, description = description, unit=unit_id)

		db.session.add(article)
		db.session.commit()



class Stock(db.Model):
	__tablename__ = 'stocks'

	id = db.Column(db.Integer, primary_key=True)
	article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), unique = True, nullable=False)
	amount = db.Column(db.Float, nullable = False)
	#todos los ultimos de cada mes se carga el registro de con cuanto esta cerrando
	created_at = db.Column(db.DateTime(), default=datetime.datetime.now())

	def __str__(self):
		return self.article_id

	@classmethod
	def create_elemt(cls, article_id, amount):
		ciere_de_mes = Stock(article = article_id, amount=amount)

		db.session.add(ciere_de_mes)
		db.session.commit()

		return ciere_de_mes



#Funcion para actualizar el stock
def updateStock(object:Stock, amount:float):
	object.amount = object.amount + amount
	object.created_at = datetime.datetime.now()
	db.session.commit()


class Consumo(db.Model):
	__tablename__ = 'consumos'

	id = db.Column(db.Integer, primary_key=True)
	person = db.Column(db.String(50), nullable=False)
	turn = db.Column(db.String(50), nullable=False)
	article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
	amount = db.Column(db.Float, nullable=False)
	date = db.Column(db.DateTime(), nullable=False)
	created_at = db.Column(db.DateTime(), default = datetime.datetime.now())

	def __str__(self):
		return str(self.article_id)

	@classmethod
	def create_element(cls, person, turn, article_id, amount, date):
		item = Consumo(person=person, turn=turn, article=article_id, amount=amount, date=date)
		db.session.add(item) #agrega registro
		db.session.commit()	#actualiza los cambios

		return item

class Carga(db.Model):
	__tablemame__ = 'cargas'

	id = db.Column(db.Integer, primary_key=True)
	person = db.Column(db.String(50), nullable=False)
	turn = db.Column(db.String(50), nullable=False)
	article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
	amount = db.Column(db.Float, nullable=False)
	date = db.Column(db.DateTime(), nullable=False)
	created_at = db.Column(db.DateTime(), default=datetime.datetime.now())

	@classmethod
	def element(cls, person, turn, article_id, amount, date):
		item = Carga(person=person, turn=turn, article=article_id, amount=amount, date=date)
		db.session.add(item)  # agrega registro
		db.session.commit()  # actualiza los cambios
		return item

class Rebajar(db.Model):
	__tablename__="rebaja"

	id = db.Column(db.Integer, primary_key=True)
	person = db.Column(db.String(50), nullable=False)
	turn = db.Column(db.String(50), nullable=False)
	article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
	amount = db.Column(db.Float, nullable=False)
	date = db.Column(db.DateTime(), nullable=False)
	observacion = db.Column(db.String(100), nullable=False)
	created_at = db.Column(db.DateTime(), default=datetime.datetime.now())

class Merma(db.Model):
	__tablename__="merma"

	id = db.Column(db.Integer, primary_key=True)
	person = db.Column(db.String(50), nullable=False)
	turn = db.Column(db.String(50), nullable=False)
	article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
	amount = db.Column(db.Float, nullable=False)
	date = db.Column(db.DateTime(), nullable=False)
	created_at = db.Column(db.DateTime(), default=datetime.datetime.now())

class Diferencia(db.Model):
	__tablename__ = 'diferencias'

	id = db.Column(db.Integer, primary_key=True)
	person = db.Column(db.String(50), nullable=False)
	turn = db.Column(db.String(50), nullable=False)
	article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
	amount = db.Column(db.Float, nullable=False)
	date = db.Column(db.DateTime(), nullable=False)
	created_at = db.Column(db.DateTime(), default = datetime.datetime.now())

	def __str__(self):
		return str(self.article_id)

	@classmethod
	def create_element(cls, person, turn, article_id, amount, date):
		item = Diferencia(person=person, turn=turn, article=article_id, amount=amount, date=date)
		db.session.add(item) #agrega registro
		db.session.commit()	#actualiza los cambios
		return item

def consulta_range(init:str, end:str):
	pass
	#article = db.session.query(Article).all() # selecciona todos los articulos

	#query = True
	#for i in article: #itera la lista de articulos que arrojo la consulta a la tabla articulo
		# se crea la consulta de la tabla articulo y articulos consumidos
	#	query = db.session.query(Article).join(Consumo).filter(Article.id == i.id,
	#	                                                       Consumo.date > init,
	#	                                                       Consumo.date < end)
	#	for row in query:
	#		for c in row.consumo_insumos:
	#			print(c.date, row.name, c.amount, c.person)

	#return [article, query]

def query_consumo_articulo(article_id, init, end):
	query = db.session.query(Article).join(Consumo).filter(Article.id == article_id,
														   Consumo.date > init,
														   Consumo.date < end).all()

	print(init, end)
	for row in query:
		for c in row.consumo_insumos:
			print(c.date, row.name, c.amount, c.person)
	return query

def StockDeUnaFechaDada(id, fecha):


	"""
	Recibe el id de un articulo y un objeto datatime
	con el formato %Y-%m-%d

	"""
	consumo = 0 #conteneder
	carga = 0   #contenedor
	if True: # carga desde el inicio de los tiempo
		query = Carga.query.filter(Carga.article_id==id,
		                           Carga.date < fecha)
		for i in query:
			print(f'carga a la fecha {i.date}')
			carga += i.amount

	if True: # consumo desde el inicio de los tiempos
		x = Consumo.query.order_by(Consumo.date)
		for i in x:
			if (i.article_id == id and i.date < fecha):
				print(f'consumo a la fecha {i.date}')
				consumo += i.amount
	print( f' Total Cargado | Total Consumido \n       {carga}   |      {consumo}'
	       f'\n diferencia : {carga - consumo}' )
	return carga-consumo

def consumoArtRangoDeFecha(id, init, end):
	query = Consumo.query.filter(Consumo.article_id==id,
	                             Consumo.date.between(init, end))

	consumo = 0
	for i in query:
		consumo += i.amount
		print(f'Consumo en rango del id={id}: {i.amount}')
	print(f'total consumido id={id}: {consumo}')
	return consumo

def cargaArtRangoDeFecha(id, init, end):
	query = Carga.query.filter(Carga.article_id==id,
	                             Carga.date.between(init, end))

	carga = 0
	for i in query:
		carga += i.amount
		print(f'Carga en rango del id={id}: {i.amount}')
	print(f'total cargado del id={id}: {carga}')

	return carga

def consultaDetallada(articulo, date):
	id = db.session.query(Article).filter(Article.name==articulo[0] )




	x = db.session.query(Article.name, Consumo.amount, Article.unit_id, Consumo.date, Consumo.turn).filter(
		Article.id==id[0].id, Article.id==Consumo.article_id,
		Consumo.date>=date[0], Consumo.date<=date[1]).order_by(Consumo.date)
	aux = ('name', 'amount', 'unit', 'date', 'turn')
	diccionario = []
	for tup in x:
		# tup es una tupla con todos los datos
		i = list(tup)
		diccionario.append({aux: i for (aux, i) in zip(aux, i)})
	print(articulo)
	return diccionario

def consultaPorMes(fecha):
	articulos = db.session.query(Article)
	a = dict()
	a["consumo"] = dict()
	a["carga"] = dict()
	a["inicio"] = dict()
	a["cierre"] = dict()
	a["diferencia"] = dict()

	for i in articulos:
		j = db.session.query(func.sum(Carga.amount)).filter(Carga.article_id == i.id,
															Carga.date < fecha[0])

		k = db.session.query(func.sum(Consumo.amount)).filter(Consumo.article_id == i.id,
															Consumo.date <= fecha[0])
		aux = [tuple(row) for row in j]  # return una tupla dentro de una list

		auxC = [tuple(row1) for row1 in k]  # return una tupla dentro de una list

		if auxC[0][0] == None:
			auxC=0
		else:
			auxC = float(format(auxC[0][0], '.2f'))
		if aux[0][0] == None:
			aux = 0
		else:
			aux = float(format(aux[0][0], '.2f'))

		try:
			if i.name == "amplificacion" or i.name == "amplificacion24":

				if i.name == "amplificacion":

					a["inicio"]["Reactivo 96"] = aux - auxC
				else:
					a["inicio"]["Reactivo 24"] = aux- auxC
			else:


				a["inicio"][str(i.name).capitalize()] = aux - auxC
		except TypeError:
			print(i.name)


		#a["inicio"][i.name] = aux[0][0]  # una tupla dentro de un list


	for i in articulos:
		j = db.session.query(func.sum(Carga.amount)).filter(Carga.article_id == i.id,
															  Carga.date >= fecha[0],
															  Carga.date <= fecha[1])
		aux = [tuple(row) for row in j]  # return una tupla dentro de una list
		if aux[0][0] == None:
			aux = 0
		else:
			aux = float(format(aux[0][0], '.2f'))
		if i.name == "amplificacion" or i.name == "amplificacion24":
			if i.name == "amplificacion":
				a["carga"]["Reactivo 96"] = aux
			else:
				a["carga"]["Reactivo 24"] = aux
		else:
			a["carga"][str(i.name).capitalize()] = aux
		#a["carga"][i.name] = aux[0][0]  # una tupla dentro de un list

	for i in articulos:
		j = db.session.query(func.sum(Diferencia.amount)).filter(Diferencia.article_id == i.id,
															  Diferencia.date >= fecha[0],
															  Diferencia.date <= fecha[1])
		aux = [tuple(row) for row in j]  # return una tupla dentro de una list
		if aux[0][0] == None:
			aux = 0
		else:
			aux = float(format(aux[0][0], '.2f'))
		if i.name == "amplificacion" or i.name == "amplificacion24":
			if i.name == "amplificacion":
				a["diferencia"]["Reactivo 96"] = aux
			else:
				a["diferencia"]["Reactivo 24"] = aux
		else:
			a["diferencia"][str(i.name).capitalize()] = aux
		#a["carga"][i.name] = aux[0][0]  # una tupla dentro de un list

	for i in articulos:
		j = db.session.query(func.sum(Consumo.amount)).filter( Consumo.article_id==i.id,
															   Consumo.date>=fecha[0],
															   Consumo.date<=fecha[1])
		aux = [tuple(row) for row in j] # return una tupla dentro de una list
		#a[""][str(i.name).capitalize()] = float(format(aux, '.2f'))  # una tupla dentro de un list
		if aux[0][0] == None:
			aux = 0
		else:
			aux = float(format(aux[0][0], '.2f'))
		try:
			if i.name == "amplificacion" or i.name == "amplificacion24":
				if i.name == "amplificacion":
					a["consumo"]["Reactivo 96"] = aux
					a["cierre"]["Reactivo 96"] = int(a["inicio"]["Reactivo 96"] - aux + a["carga"]["Reactivo 96"] + a["diferencia"]["Reactivo 96"])
				else:
					a["consumo"]["Reactivo 24"] = aux
					a["cierre"]["Reactivo 24"] = int(a["inicio"]["Reactivo 24"] - aux + a["carga"]["Reactivo 24"] + a["diferencia"]["Reactivo 24"])
			else:
				a["consumo"][str(i.name).capitalize()] = aux
				a["cierre"][str(i.name).capitalize()] = int(a["inicio"][str(i.name).capitalize()] - aux + a["carga"][str(i.name).capitalize()] + a["diferencia"][str(i.name).capitalize()])
			#a["consumo"][i.name] = aux[0][0]  # una tupla dentro de un list
		except TypeError:
			continue


			#a["cierre"][i.name] = a["inicio"][i.name] - aux[0][0] + a["carga"][i.name]  # una tupla dentro de un list

	return a # return dict



