from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from registration.forms import SignUpForm
from registration.models import Profile

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()  # load the profile instance created by the signal
			user.profile.university = form.cleaned_data.get('university')
			user.profile.birth_date = form.cleaned_data.get('birth_date')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('/')
	else:
		form = SignUpForm()
	return render(request, 'registration/signup.html', {'form': form})

def view_profile(request, pk):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)
		
		sub_courses = profile.courses.all()

		activities = []
		for course in sub_courses:
			for l in course.link.all()[:10]:
				if l.user.id == profile.id:
					activities.append({'obj': l, 'tipo': 'um link'})
			for l in course.list.all()[:10]:
				if l.user.id == profile.id:
					activities.append({'obj': l, 'tipo': 'uma lista'})
			for s in course.summary.all()[:10]:
				if s.user.id == profile.id:
					activities.append({'obj': s, 'tipo': 'um resumo'})

		activities.sort(key = lambda x: x['obj'].date, reverse=True)
		activities = activities[:10]

		context = {
			'profile': profile,
			'courses': sub_courses,
			'activities': activities
		}
		
		return render(request, 'registration/perfil.html', context)

	return redirect('login')

def edit_profile(request, pk):
	profile = Profile.objects.get(pk=pḱ)
	if request.user.username == profile.username:
		form = ProfileForm(instance=profile)
		if request.method == "POST" and form.is_valid():
			profile = form.save(commit=False)
			profile.save()
			return redirect('ROTA DE REDIRECT AQUI')

		return render(request, 'TEMPLATE', {'form':form, 'profile':profile})
	#TODO colocar erro de permissao
	# return ALGUM ERRO AQUI
