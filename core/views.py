## from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

html_base = """
    <h1>Mi Primer Menú</h1>
    <ul>
        <li><a href="/">Portada</a>
        <li><a href="/about-me/">Acerca de</a>
        <li><a href="/contact/">Contacto</a>
    </ul>
"""

# relaciona la parte vista con el template home.html
def home(request, plantilla="home.html"):

#    http_response = "<h1>Pagina de Inicio</h1>"
#    http_response = html_base + http_response
#    return HttpResponse(http_response)
    return render(request, plantilla)

def aboutme(request, plantilla="aboutme.html"):
	
#    http_response = "<h1>Pagina de Acerca De</h1>"
#    http_response = html_base + http_response
#    return HttpResponse(http_response)
    return render(request, plantilla)

def contact(request, plantilla="contact.html"):

#    http_response = "<h1>Pagina de Contacto</h1>"
#    http_response = html_base + http_response
#    return HttpResponse(http_response)
    return render(request, plantilla)

def portafolio(request, plantilla="portafolio.html"):

#    http_response = "<h1>Pagina de Contacto</h1>"
#    http_response = html_base + http_response
#    return HttpResponse(http_response)
    return render(request, plantilla)