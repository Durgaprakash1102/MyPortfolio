from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'skill_list.html', {'skills': skills})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def certification_list(request):
    certifications = Certification.objects.prefetch_related('images').all()
    return render(request, 'certification_list.html', {'certifications': certifications})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to the database
            messages.success(request, 'Thank you! Your message has been sent.')
            return redirect('contact')  # Redirect to clear POST data and prevent resubmission
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def contact_list(request):
    contacts = Contact.objects.order_by('-created_at')  
    return render(request, 'contact_list.html', {'contacts': contacts})