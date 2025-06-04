from django.conf import settings
from django.db import models
from django.utils import timezone


class Template(models.Model):
    """Report template such as 'Ultimate Guide'."""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Report(models.Model):
    """User generated report."""
    TONE_CHOICES = [
        ('confident', 'Confident'),
        ('rebellious', 'Rebellious'),
        ('nurturing', 'Nurturing'),
    ]
    PERSONA_CHOICES = [
        ('executive', 'Executive'),
        ('mentor', 'Mentor'),
        ('disruptor', 'Disruptor'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    audience = models.CharField(max_length=200)
    tone = models.CharField(max_length=20, choices=TONE_CHOICES)
    persona = models.CharField(max_length=20, choices=PERSONA_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.template.name} for {self.topic}"


class Section(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
