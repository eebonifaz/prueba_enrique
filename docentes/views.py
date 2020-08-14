from django.shortcuts import render, redirect
from .forms import DocenteForm
from .models import Docentes
# Crear

def creardocente( request, plantilla="docentes/creardocente.html"):
	# return render(request, plantilla)
	if request.method == "POST":
		docenteForm = DocenteForm( request.POST )
		if docenteForm.is_valid():
			docenteForm.save()
			return redirect('docente')
	else:
		docenteForm = DocenteForm()
	return render(request, plantilla, {'docenteform':docenteForm})


#Modificar
def modificardocente(request, plantilla="modificardocente.html"):
	return render(request, plantilla)
#Eliminar
def eliminardocente(request, plantilla="eliminardocente.html"):
	return render(request, plantilla)
#Consultar
def editardocente(request, plantilla="editardocente.html"):
	return render(request, plantilla)


#Consultar
def docente(request, plantilla="docentes/docentes.html"):
	docentes_list = Docentes.objects.all()
	return render(request, plantilla, {'docentes_list':docentes_list})
