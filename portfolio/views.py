from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def admin(request):
    return render(request, 'portfolio/admin.html')

def admin_add_product(request):
    return render(request, 'portfolio/admin_add_product.html')

def admin_add_user(request):
    return render(request, 'portfolio/admin_add_user.html')

def admin_add_client(request):
    return render(request, 'portfolio/admin_add_client.html')

def transaction(request):
    return render(request, 'portfolio/transaction.html')

def transaction_detail(request):
    return render(request, 'portfolio/transaction_detail.html')

def invent_report(request):
    return render(request, 'portfolio/invent_report.html')

def view_product(request):
    return render(request, 'portfolio/view_product.html')