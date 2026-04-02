from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Report
from .forms import ReportForm

@login_required
def submit_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            messages.success(request, f'Report submitted! Your reference number is {report.reference_number}')
            return redirect('dashboard')
    else:
        form = ReportForm()
    return render(request, 'reports/report_form.html', {'form': form})

@login_required
def dashboard(request):
    reports = Report.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'reports/dashboard.html', {'reports': reports})

@login_required
def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk, user=request.user)
    return render(request, 'reports/report_detail.html', {'report': report})