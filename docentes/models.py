from django.db import models

# Create your models here.

class Docentes( models.Model ):
	id = models.AutoField( primary_key = True )
	nombre = models.CharField("Nombre", max_length = 200)
	apellido = models.CharField("Apellido", max_length = 200)
	edad = models.IntegerField()
	email = models.EmailField()
	sexo = models.CharField("Sexo", max_length = 1)
	user = models.CharField("user", max_length = 200)
	user_mod = models.CharField("user_mod", max_length = 15)
	created = models.DateTimeField(auto_now = True)

	def __str__( self ):
		return '{0}.{1}'.format(self.apellido, self.nombre)