from flask import Blueprint, session, escape, redirect, url_for # se utiliza para importar clases

from . import models
from flask import render_template, request, jsonify #se utiliza para import funsiones.
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import RegisterForm
from datetime import datetime
#",ProductoForm"
from .models import User, Consumo, Article, Carga, Stock, updateStock, StockDeUnaFechaDada, consumoArtRangoDeFecha, cargaArtRangoDeFecha, consultaPorMes, Diferencia



page = Blueprint('page', __name__) #Se almacenan las rustas en esta instancia

@page.route('/', methods=['GET', 'POST'])
def Consumos():
	if request.method == "POST":
		if request.form:
			articulos = ['filtro',
		            'ws2',
		            'colectores',
		            'ependrorf05',
		            'ependrorf02',
		            'ependrorf2',
					'amplificacion',
		            'puntas10',
		            'puntas1000',
		            'ws1',
		            'ssb',
		            'eb',
		            'hisopos',
		            'amplificacion24']

		for articulo in articulos:
			aux = Article.query.filter_by(name=articulo).first()
			if (request.form[articulo] != ""):
				if (float(request.form[articulo]) > 0):
					Consumo.create_element(person = request.form['nombre'],
									   turn = request.form['turno'],
									   article_id = aux,
									   amount = float(request.form[articulo]),
									   date = request.form['fecha'])
					stock = Stock.query.filter_by(article_id=aux.id).first()
					updateStock(object=stock, amount=(-1*float(request.form[articulo]))) #pasa un numero negativo ya que decrementa el inventario

		return redirect("/")

	return render_template('index.html', title='Bienvenido')

@page.app_errorhandler(404)
def page_not_found(error):
	# por convencion los errores se manejas de la siguiente forma,
	# una descripcion del error y el numero del error
	return render_template('errors/404.html', name='Leonardo'), 404


#Los metodos por los cuales podra ser consultada esta url
@page.route('/index', methods=['GET', 'POST']) #SE LE INDICA con que methodos trabajara esta url
def login():
	#form = LoginForm(request.form) #esto permite que cuando se envie informacion del formulario, se capture en la instancia.

	#if request.method == 'POST' and form.validate():
	if request.method == 'POST':
		#el atributo data es el metodos atraver del cual se obtiene el valor que usuario esta enviando al servidor
		user = models.User.query.filter_by(username=request.form['username']).first()

		#cuidar el orden con el que se declaran los argumentos de check_password_hash
		if user and check_password_hash(user.password, request.form['pws']):
			session['username'] = user.username  # asi se crea la cookie de session
			print('Nueva sesion creada!')
			return redirect('/home')
		return "Datos invalidos"



@page.route('/register/', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)

	if request.method == 'POST':
		if form.validate():

			hash_pw = generate_password_hash(form.password.data, method="sha256")
			User.crear_element(form.username.data, hash_pw)
			#redirect, redirecciona a una url
			return redirect("/")

	return render_template('auth/register.html', title="Register", form=form)

@page.route('/home')
def home():
	if 'username' in session: # asi se valida que existe la sesion
		#return "You're %s" % escape(session['username'])
		return render_template('sesion.html', title='Login')
	return "debes loguearte"


@page.route('/logout')
def logout():
	session.pop('username', None)
	#return 'Su sesion fue cerrada satisfactoriamente.'
	return redirect("/")

@page.route('/url_for/uso')
def uso():
	return redirect(url_for('page.home')) #url_for recibe un nombre de una funcion y retorna su ruta.
			#cuando se esta usando programacion modular y se desea usar el metodo url_for, debe colocarse
			# como se muestra en el ejemplo
			#de no sere modular con blueprint se usa sin page.*

@page.route('/cargar', methods=["GET", "POST"])
def cargar():
	if 'username' in session:
		if request.method == "POST":
			articulos = ['filtro',
						 'ws2',
						 'colectores',
						 'ependrorf05',
						 'ependrorf02',
						 'ependrorf2',
						 'puntas10',
						 'puntas1000',
						 'amplificacion',
						 'ws1',
						 'ssb',
						 'eb',
						 'hisopos',
						 'amplificacion24']
			for articulo in articulos:
				aux = Article.query.filter_by(name=articulo).first()
				if (request.form[articulo] != ""):
					if (float(request.form[articulo]) > 0):
						Carga.element(person = request.form['nombre'],
										   turn = request.form['turno'],
										   article_id = aux,
										   amount = float(request.form[articulo]),
										   date = request.form['fecha'])

						stock = Stock.query.filter_by(article_id=aux.id).first()
						updateStock(object=stock, amount=float(request.form[articulo])) #pasa un numero negativo ya que decrementa el inventario



		return render_template("sesion.html", title="Home")
	return "debes loguearte"


from datetime import datetime
@page.route('/consultaConsumo', methods=["GET", "POST"])
def consulta_consumo():
	if 'username' in session:
		if request.method == "POST":
			init = datetime.strptime(str(request.form['inicio']), "%Y-%m-%d")  # casting de str a datetime
			end = datetime.strptime(str(request.form['fin']), "%Y-%m-%d")  # casting de str a datetime
			article = Article.query.all()
			contenedor = []
			if (init <= end):
				for q in article:
					_c =[q.name]
					_c.append(float(format(StockDeUnaFechaDada(q.id, init), '.2f'))) #se formatea el float para que tenga una presicion de 1
					_c.append(float(format(consumoArtRangoDeFecha(q.id, str(init), str(end)),'.2f')))
					_c.append(float(format((_c[1] + (cargaArtRangoDeFecha(q.id, str(init), str(end)) -_c[2])), '.2f')))

					contenedor.append(_c)

			return render_template('tabla_consulta.html', titlce="consulta", consulta = contenedor)
		return render_template('consumo.html', title="consulta")
	return "debes loguearte"

@page.route('/inv', methods=['GET', 'POST'])
def inv():
	stock = Stock.query.all()
	consulta = []
	for row in stock:
		arti = []
		arti.append(row.id)
		aName = Article.query.filter_by(id=row.article_id).first()
		aName = aName.name
		arti.append(aName)
		arti.append(row.amount)
		arti.append(row.created_at)
		consulta.append(arti)

	return render_template('inventario.html', title="Inventario", consulta=consulta)


@page.route('/casalab')
def casaLab():
	StockDeUnaFechaDada(9, datetime.strptime('2022-01-31', "%Y-%m-%d"))
	consumoArtRangoDeFecha(9, '2022-01-1', '2022-01-31')

	return render_template('vistaHomeCorporativa.html', title="Inventario")

@page.route('/consumo', methods=['GET', 'POST'])
def consumoDetallado():
	if 'username' in session:
		if request.method=='POST':
			date = []
			date.append(str(datetime.strptime(str(request.form['inicio']), "%Y-%m-%d")))
			date.append(str(datetime.strptime(str(request.form['fin']), "%Y-%m-%d")))
			#models.db.Query(Article).join(Consumo).filter()
			articulos = request.form.getlist('articulo')
			diccionario = models.consultaDetallada(articulos, date)
			return render_template('dataTable.html', diccionario=diccionario, date=date)

		return render_template('formConsulta.html')

@page.route('/t', methods=['GET', 'POST'])
def consumoMensual():
	if 'username' in session:
		f = 28
		mes = {
			"enero": [1, 31],
			"febrero": [2, f],
			"marzo": [3, 31],
			"abril": [4, 30],
			"mayo": [5, 31],
			"junio": [6, 30],
			"julio": [7, 31],
			"agosto": [8, 31],
			"septiembre": [9, 30],
			"octubre": [10, 31],
			"noviembre": [11, 30],
			"diciembre": [12, 31]
		}
		if request.method=="POST":
			ano = int(request.form['ano'])

			if (ano%4 == 0) and not (ano%100 == 0) and (ano%400 == 0):
				f = 29

			fecha = [f"{ano}-{mes[request.form.getlist('mes')[0]][0]}-01",
					 f"{ano}-{mes[request.form.getlist('mes')[0]][0]}-{mes[request.form.getlist('mes')[0]][1]}"]

			d = consultaPorMes(fecha)
			return render_template("dataTable_consumoMes.html", dicc=d, key=d["consumo"].keys(), ano=ano, mes=request.form["mes"])

		if request.method=="GET":
			return render_template("consumoMensual.html", mes=mes.keys())

@page.route('/diferencias', methods=['GET', 'POST'])
def diferencias():

	if request.method == "POST":
		articulos = ['filtro',
					 'ws2',
					 'colectores',
					 'ependrorf05',
					 'ependrorf02',
					 'ependrorf2',
					 'puntas10',
					 'puntas1000',
					 'amplificacion',
					 'ws1',
					 'ssb',
					 'eb',
					 'hisopos',
					 'amplificacion24']
		for articulo in articulos:
			aux = Article.query.filter_by(name=articulo).first()
			if (request.form[articulo] != ""):
				if (float(request.form[articulo]) < 0 or float(request.form[articulo]) > 0  ):
					Diferencia.create_element(person = request.form['nombre'],
											  turn = request.form['turno'],
											  article_id = aux,
											  amount = float(request.form[articulo]),
											  date = request.form['fecha'])

	return render_template("cargar.html")



"""
def merma():
	if 'username'in session:
		if request.method=='POST':
			if ( request.form['inicio'] != '' and resquest.form['fin'] != '' ): 
				rangoFecha = [request.form['inicio']]
				ranfoFecha.append[request.form['fin']]
				
				if (request.form['articulo') and request.form['person']	):
					 session.Querty
				
			
		


"""



