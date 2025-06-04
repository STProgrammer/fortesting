from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from socialapp.models import Profile

class Command(BaseCommand):
    help = 'Create a demo user with profile.'

    def handle(self, *args, **options):
        username = 'demo'
        password = 'demo123'
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f"User '{username}' already exists"))
            return
        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user)
        self.stdout.write(self.style.SUCCESS(
            f"Created demo user '{username}' with password '{password}'"))
