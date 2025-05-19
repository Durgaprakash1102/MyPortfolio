from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

def home(request):
    latest_resume = Resume.objects.order_by('-uploaded_at').first()
    return render(request, "home.html", {"latest_resume": latest_resume})
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

def analytics_dashboard(request):
    visits_per_day = VisitorLog.objects.annotate(date=TruncDate('timestamp')).values('date').annotate(visits=Count('id')).order_by('-date')
    top_pages = VisitorLog.objects.values('path').annotate(visits=Count('id')).order_by('-visits')[:10]
    linkedin_visits = VisitorLog.objects.filter(referrer__icontains='linkedin.com').count()
    top_clicks = VisitorLog.objects.exclude(clicked_element__isnull=True).values('clicked_element').annotate(total=Count('id')).order_by('-total')[:10]

    return render(request, 'analytics_dashboard.html', {
        'visits_per_day': visits_per_day,
        'top_pages': top_pages,
        'linkedin_visits': linkedin_visits,
        'top_clicks': top_clicks
    })

@csrf_exempt
def track_click(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ip = request.META.get('REMOTE_ADDR')
        log = VisitorLog.objects.filter(ip_address=ip).order_by('-timestamp').first()
        if log:
            log.clicked_element = data.get('element', 'Unknown')
            log.save()
    return JsonResponse({'status': 'ok'})

from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST
from django.contrib.auth import logout
@never_cache
def logout_view(request):
    logout(request)
    response = redirect('login')  # or wherever you want to redirect after logout
    # Add no-cache headers explicitly (optional, because @never_cache sets these)
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response