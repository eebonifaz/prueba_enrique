from django.forms import ModelForm
from .models import Docentes

class DocenteForm( ModelForm ):
	def __init__(self, *args, **kwargs):
		super(DocenteForm, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
		})
	class Meta:
		model = Docentes
		fields = [ 'nombre', 'apellido', 'edad', 'email', 'sexo' ]