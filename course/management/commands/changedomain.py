from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp


class Command(BaseCommand):
    help = 'Changes current domain'

    def add_arguments(self, parser):
        parser.add_argument('domain', type=str)

    def handle(self, *args, **options):
        Site.objects.all().delete()
        SocialApp.objects.all().delete()

        site = Site(id=0, domain=options['domain'], name='custom')
        site.save()

        google = SocialApp(
            provider='google',
            name='Google',
            client_id='391769807258-1m9ojltdvphurdmuslv4\
        aoriq4jkc5p5.apps.googleusercontent.com',
            secret='KtzOBNQTsof9fkGlB8iC5rLK'
        )
        google.save()
        google.sites.set([site.id])

        self.stdout.write(self.style.SUCCESS('Succesfully changed domain'))
