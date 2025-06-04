from django.conf import settings
from django.db import models
from django.utils import timezone


class Format(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Persona(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Report(models.Model):
    FORMAT_CHOICES = [
        ('guide', 'Ultimate Guide'),
        ('mistakes', 'Top 10 Mistakes'),
        ('secrets', 'Insider Secrets'),
    ]

    TONE_CHOICES = [
        ('confident', 'Confident'),
        ('rebellious', 'Rebellious'),
        ('nurturing', 'Nurturing'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports')
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES)
    topic = models.CharField(max_length=200)
    audience = models.CharField(max_length=200, blank=True)
    tone = models.CharField(max_length=20, choices=TONE_CHOICES, blank=True)
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.get_format_display()} - {self.topic}'
