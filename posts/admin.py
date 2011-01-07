#!_*_ coding: utf8 _*_

from posts.models import Artigo
from posts.models import Categoria
from django.contrib import admin

class ArtigoAdmin(admin.ModelAdmin):
	#fields = ['publicacao', 'titulo', 'conteudo']
	fieldsets = [
		(None,                     {'fields': ['titulo', 'conteudo']}),
		('Informações adicionais', {'fields': ['publicacao'], 'classes': ['collapse']}),
	]
	list_display = ('titulo', 'categoria', 'publicacao')
	date_hierarchy = 'publicacao'
	search_fields = ['titulo']


admin.site.register(Categoria)	
admin.site.register(Artigo, ArtigoAdmin)