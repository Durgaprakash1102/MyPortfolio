
from django.contrib import admin
from django.urls import path
from Portfolio.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name="home"),
    path('about/', about , name="about"),
    path('skills/',skill_list,name="skill_list"),
    path('projects/', project_list, name='project_list'),
    path('certifications/', certification_list, name='certification_list'),
    path('contact/', contact_view, name='contact'),
    path('contacts/', contact_list, name='contact_list'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
