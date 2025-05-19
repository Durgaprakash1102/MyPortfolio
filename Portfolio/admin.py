from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Certification)
admin.site.register(CertificationImage)
admin.site.register(Contact)
admin.site.register(Resume)