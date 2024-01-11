from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SelectField, FloatField

class LoginForm(Form):
	username = StringField('Username', [
		validators.length(min=4, max=50, message="El username se encuentra fuera de rango") # esta es una funcion
	]) # crea el input del formulario, el string enviado por parametros lo mostrara en la pagina
	password = PasswordField('Password', [
		validators.DataRequired()# un metodo
	])
	unidad = SelectField('unidad', choices=[('mL', 'MiliLitro'), ('Pza', 'Piezas')])


class RegisterForm(Form):
	username = StringField('Username', [
				validators.length(min=4, max=50, message=" el usuario debe contener un numero de caracteres mayor o igual que cuatro y menor a 50")
	])
	email = StringField('email', [
						validators.length(min = 6, max=100, message="el numero de catacteres debe ser minimo 6 y maximo 100"),
						validators.DataRequired(message="Email requerido")

	])

	password = PasswordField('Password', [

							validators.DataRequired(message="password requerido"),
							validators.EqualTo('password', message="la cotrasena no conincide")
	])

	re_password = PasswordField('re-password')

	acept = BooleanField(validators.DataRequired())

class product(Form):
	name =StringField('name', [validators.length(min=2, max=25),
	                             validators.DataRequired(message="Indique nombre del producto")])
	turno = SelectField('Turno', choices=["Mañana", "Tarde", "Noche", "Todo el Dia"])
	amplificacion = IntegerField('amplificacion', [validators.DataRequired(message="Indique la cantidad")])
	reactivo = IntegerField('reactivo', [validators.DataRequired(message="Indique la cantidad")])

class corrida(Form):
	p1000 = IntegerField('Puntas 1000', [validators.DataRequired()])
	p10 = IntegerField('Puntas 10', [validators.DataRequired()])
	pAmplificacion = IntegerField('Placa Amplificacion', [validators.DataRequired()])
	pElucion = IntegerField('Placa Elucion', [validators.DataRequired()])
	pFiltro = IntegerField('Filtros', [validators.DataRequired()])
	tReactivo = IntegerField('Tubos Reactivos', [validators.DataRequired()])
	papelAdhesivo = IntegerField('Papel Adhesivo', [ validators.DataRequired()])
	hisopos = IntegerField('Hisopos', [validators.DataRequired()])
	vSSB = IntegerField('Vial SSB', [validators.DataRequired()])
	ws1 = FloatField('WS1', [validators.DataRequired(message="Indique las Unidades en mL")])
	buffer = IntegerField('Buffer', [validators.DataRequired()])
	ws2 = FloatField('Etanol', [validators.DataRequired()])

