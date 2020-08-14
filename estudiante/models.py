from django.db import models

# Create your models here.

class Estudiante( models.Model ):
	nombre = models.CharField(max_length=200)
	apellido = models.CharField(max_length=200)
	edad = models.IntegerField()
	sexo = models.CharField(max_length=1) 
	user = models.CharField(max_length=20)
	user_mod = models.CharField(max_length=20)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering: ["descripcion"]
		verbose_name = "Estudiante"
		verbose_name_plural = "Estudiantes"

	def __str__(self):
		return "{} {}".format( self.apellido, self.nombre ) 