from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.contrib.auth import get_user_model


class SocialappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'socialapp'

    def ready(self):
        User = get_user_model()

        def create_default_user(sender, **kwargs):
            if not User.objects.filter(username='demo').exists():
                User.objects.create_user('demo', password='demo123')

        post_migrate.connect(create_default_user, sender=self)
