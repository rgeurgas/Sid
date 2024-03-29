from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from course.models import Course
from registration.forms import SignUpForm, EditarForm
from registration.models import Profile


def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()  #load the profile instance created by the signal
			user.profile.university = form.cleaned_data.get('university')
			user.profile.birth_date = form.cleaned_data.get('birth_date')
			user.profile.bio = form.cleaned_data.get('bio')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('/')
	else:
		form = SignUpForm()
	return render(request, 'registration/signup.html', {'form': form})

@login_required
def view_profile(request, pk):
	if request.user.is_authenticated:
		profile = Profile.objects.get(id=pk)
		
		sub_courses = profile.courses.all()

		if request.method == 'POST':
			form = EditarForm(request.POST, request.FILES, instance=profile)
			print(request.FILES)
			if form.is_valid():
				profile = form.save(commit=False)
				profile.save()
				return redirect('view_profile', pk=profile.pk)
		else:
			form = EditarForm(instance=profile)

		activities = []
		for course in Course.objects.all():
			for l in course.link.all():
				if l.user.id == profile.user.id:
					activities.append({'obj': l, 'tipo': 'um link'})
			for l in course.list.all():
				if l.user.id == profile.user.id:
					activities.append({'obj': l, 'tipo': 'uma lista'})
			for s in course.summary.all():
				if s.user.id == profile.user.id:
					activities.append({'obj': s, 'tipo': 'um resumo'})

		activities.sort(key = lambda x: x['obj'].date, reverse=True)
		activities = activities[:5]

		print(profile.user.first_name +'>>>>' + str(len(activities)))

		context = {
			'profile': profile,
			'courses': sub_courses,
			'activities': activities,
			'form': form
		}

		return render(request, 'registration/perfil.html', context)

	return redirect('login')

@login_required
def approve_and_close(request):
	return HttpResponse('<script type="text/javascript"> window.opener.parent.location.href = "/"; window.close(); </script>')