from django.db import models

# Create your models here.
class Categoria(models.Model):
	nome = models.CharField(max_length=50)
	def __unicode__(self):
		return self.nome

class Artigo(models.Model):
	titulo = models.CharField(max_length=100)
	conteudo = models.TextField()
	publicacao = models.DateTimeField()
	categoria = models.ForeignKey(Categoria)
	def __unicode__(self):
		return self.titulo
