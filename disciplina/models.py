from django.db import models

class Disciplina(models.Model):
	nome = models.CharField(max_length=100, null=False)
	codigo = models.CharField(max_length=8, null=False, unique=True)
	listas = models.ManyToManyFields(Lista)
	resumos = models.ManyToManyFields(Resumos)
	links = models.ManyToManyFields(Links)

class Tag(models.Model):
	nome = models.CharField(max_length=50)

class Arquivo(models.Model):
	nome = models.CharField(max_length=100)
	arquivo = models.FileField(upload_to=lambda instace, filename: 'uploads/{instance.user.id}/{filename}')

class Lista(models.Model):
	nome = models.CharField(max_length=100, null=False)
	professor = models.CharField(max_length=100)
	tags = models.ManyToManyFields(Tag)
	arquivos = models.ManyToManyFields(Arquivo)
	disciplina = models.ManyToManyFields(Disciplina)

class Resumo(models.Model):
	nome = models.CharField(max_length=100, null=False)
	professor = models.CharField(max_length=100)
	tags = models.ManyToManyFields(Tag)
	arquivos = models.ManyToManyFields(Arquivo)
	disciplina = models.ManyToManyFields(Disciplina)

class Link(models.Model):
	nome = models.CharField(max_length=100, null=False)
	descricao = models.TextField()
	link = models.CharField(max_length=100)
	professor = models.CharField(max_length=100)
	tags = models.ManyToManyFields(Tag)
