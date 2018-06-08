from django import forms

from .models import Post

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ('nome', 'codigo')

class Lista(models.Model):
	class Meta:
		model = Lista
		fields('nome', 'professor', 'tags', 'arquivos', 'disciplina')

class Resumo(models.Model):
	class Meta:
		model = Resumo
		fields('nome', 'professor', 'tags', 'arquivos', 'disciplina')

class Link(models.Model):
	class Meta:
		model = Link
		fields('nome', 'descricao', 'link', 'professor', 'tags')
