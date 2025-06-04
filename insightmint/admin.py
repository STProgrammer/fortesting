from django.contrib import admin
from .models import Template, Report, Section


class SectionInline(admin.TabularInline):
    model = Section
    extra = 0


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("template", "topic", "user", "created_at")
    inlines = [SectionInline]
