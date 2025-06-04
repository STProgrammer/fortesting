from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


def create_templates(apps, schema_editor):
    Template = apps.get_model('insightmint', 'Template')
    for name in ['Ultimate Guide', 'Top 10 Mistakes', 'Insider Secrets']:
        Template.objects.create(name=name)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('audience', models.CharField(max_length=200)),
                ('tone', models.CharField(choices=[('confident', 'Confident'), ('rebellious', 'Rebellious'), ('nurturing', 'Nurturing')], max_length=20)),
                ('persona', models.CharField(choices=[('executive', 'Executive'), ('mentor', 'Mentor'), ('disruptor', 'Disruptor')], max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insightmint.template')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='insightmint.report')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.RunPython(create_templates),
    ]
