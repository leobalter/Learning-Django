# Create your views here.
# -*- coding: utf-8 -*- 
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from posts.models import Artigo
from django.http import HttpResponse
from django.http import Http404

def index(request):
	lista_ultimos_artigos = Artigo.objects.all().order_by('-publicacao')[:5]
	return render_to_response('dicas/index.html', {'lista_ultimos_artigos': lista_ultimos_artigos})
	
def detail(request, post_id):
	d = get_object_or_404(Artigo, pk=post_id)
	return render_to_response('dicas/detail.html', {'dica': d})