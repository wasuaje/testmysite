# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from nomina.models import CfBanco

def list_form(request):
    return render_to_response('list_form.html')

def list(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        bancos = CfBanco.objects.filter(nombre__icontains=q)
        return render_to_response('search_results.html',
            {'bancos': bancos, 'query': q})
    else:
        return render_to_response('list_form.html', {'error': True})
