from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ReportForm
from .models import Template, Report, Section


def landing(request):
    templates = Template.objects.all()
    return render(request, 'insightmint/landing.html', {'templates': templates})


@login_required
def create_report(request, template_id):
    template = get_object_or_404(Template, id=template_id)
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.template = template
            report.save()
            _populate_default_sections(report)
            return redirect('report_detail', report_id=report.id)
    else:
        form = ReportForm()
    return render(request, 'insightmint/create_report.html', {'form': form, 'template': template})


@login_required
def report_detail(request, report_id):
    report = get_object_or_404(Report, id=report_id, user=request.user)
    return render(request, 'insightmint/report_detail.html', {'report': report})


@login_required
def onboarding(request):
    """Simple walkthrough placeholder."""
    steps = [
        "Choose a template",
        "Enter topic and audience",
        "Generate report",
        "Edit and export",
    ]
    return render(request, 'insightmint/onboarding.html', {'steps': steps})


def _populate_default_sections(report):
    titles = ['Introduction', 'Problem', 'Case Study', 'CTA']
    for idx, title in enumerate(titles):
        Section.objects.create(report=report, title=title, order=idx)
