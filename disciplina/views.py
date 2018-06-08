from django.shortcuts import render

from .forms import DisciplinaForm

def disciplinas(request):
	disciplinas = Disciplina.objects.all()
	data = {}
	data['object_list'] = disciplinas
	return render(request, 'disciplina/index.html', data)

def disciplina_details(request, pk):
	d = Disciplina.objects.get(pk=pk)
	return render(request, 'disciplina/detail.html', {'disciplina':d})

def disciplina_new(request):
	if request.method == "POST":
		form = DisciplinaForm(request.POST)
		if form.is_valid():
			disciplina = form.save(commit=False)
			disciplina.save()
			return redirect('disciplina', pk=disciplina.pk)
	else:
		form = DisciplinaForm()
	return render(request, 'disciplina/index.html', {'form':form})
