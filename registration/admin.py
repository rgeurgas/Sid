from django.contrib import admin

from registration.models import Profile

class ProfileAdmin(admin.ModelAdmin):
	fieldset = [
		(None, {'fields':['username']}),
		(None, {'fields':['university']}),
		(None, {'fields':['birth_date']}),
	]

admin.site.register(Profile, ProfileAdmin)
