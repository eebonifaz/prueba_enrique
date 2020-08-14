from django.db import models

# Create your models here.

class Producto( models.Model ):
	descripcion = models.CharField(max_length=100)
	precio = models.IntegerField()
	user = models.CharField(max_length=15)
	user_mod = models.CharField(max_length=15)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering: ["descripcion"]
		verbose_name = "Producto"
		verbose_name_plural = "Productos"

	def __str__(self):
		return self.descripcion