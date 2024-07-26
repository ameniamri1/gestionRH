from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import LeaveRequestForm
from .models import Leave, Employee
from django.http import HttpResponse
from django.contrib import messages

@login_required
def request_leave(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            try:
                leave.employee = request.user.employee
            except Employee.DoesNotExist:
                messages.error(request, "Aucun employé associé à cet utilisateur.")
                return redirect('request_leave')
            leave.save()
            messages.success(request, "Votre demande de congé a été soumise avec succès.")
            return redirect('leave_request_status')
    else:
        form = LeaveRequestForm()
    return render(request, 'leave_management/request_form.html', {'form': form})

@login_required
def leave_request_status(request):
    try:
        leaves = Leave.objects.filter(employee=request.user.employee)
    except Employee.DoesNotExist:
        messages.error(request, "Aucun employé associé à cet utilisateur.")
        return redirect('home')
    return render(request, 'leave_management/leave_status.html', {'leaves': leaves})

@login_required
def approve_leave(request, leave_id):
    leave = get_object_or_404(Leave, pk=leave_id)
    if request.method == "POST":
        leave.status = 'Approved'
        leave.save()
        send_notification_to_employee(leave)
        return redirect('leave_request_status')
    return render(request, 'leave_management/approve_leave.html', {'leave': leave})

@login_required
def reject_leave(request, leave_id):
    leave = get_object_or_404(Leave, pk=leave_id)
    if request.method == "POST":
        leave.status = 'Rejected'
        leave.save()
        send_notification_to_employee(leave)
        return redirect('leave_request_status')
    return render(request, 'leave_management/reject_leave.html', {'leave': leave})

def send_notification_to_employee(leave):
    send_mail(
        'Statut de votre demande de congé',
        f'Votre demande de congé pour {leave.leave_type} du {leave.start_date} au {leave.end_date} a été {leave.status.lower()}.',
        'from@example.com',
        [leave.employee.email],
        fail_silently=False,
    )

def leave_request_view(request):
    if request.method == "POST":
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = LeaveRequestForm()
    return render(request, 'leave_management/leave_form.html', {'form': form})

def home(request):
    return redirect('request_leave')

def success_page(request):
    return render(request, 'leave_management/success.html')



# leave_management/views.py

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import TemplateDoesNotExist

def test_template(request):
    try:
        template = get_template('leave_management/leave_form.html')
        return HttpResponse("Template found")
    except TemplateDoesNotExist:
        return HttpResponse("Template does not exist")
