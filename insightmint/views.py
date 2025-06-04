from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ReportForm
from .models import Report


def landing(request):
    """Simple marketing page previewing the product."""
    return render(request, 'insightmint/landing.html')


@login_required
def onboarding(request):
    """Display onboarding steps after signup."""
    return render(request, 'insightmint/onboarding.html')


@login_required
def report_create(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            if not report.content:
                report.content = generate_report_content(report)
            report.save()
            return redirect('report_detail', pk=report.pk)
    else:
        form = ReportForm()
    return render(request, 'insightmint/report_form.html', {'form': form})


@login_required
def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk, user=request.user)
    return render(request, 'insightmint/report_detail.html', {'report': report})


def generate_report_content(report):
    """Very basic simulated content generator."""
    intro = f"Introducing {report.topic} for {report.audience}."
    body = f"Here are insights on {report.topic} in a {report.tone} tone."
    closing = "Ready to take action?"
    return "\n\n".join([intro, body, closing])
