from django.db import models
class Skill(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skills/')

    def __str__(self):
        return self.name

class Project(models.Model):
    PROJECT_TYPE_CHOICES = [
        ('development', 'Development'),
        ('deployment', 'Deployment'),
        ('devops', 'DevOps'),
        ('designing', 'Designing'),
    ]

    title = models.CharField(max_length=200)
    technology_stack = models.TextField()
    url = models.URLField(blank=True)
    description = models.TextField()
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPE_CHOICES, default='development')

    def __str__(self):
        return self.title

from django.db import models

class Certification(models.Model):
    name = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=255)
    issue_date = models.DateField()
    credential_id = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.issuing_organization}"

class CertificationImage(models.Model):
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='certification_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.certification.name}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name