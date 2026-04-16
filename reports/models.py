from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    CATEGORY_CHOICES = [
        ('pothole', 'Pothole'),
        ('water_leak', 'Water Leak'),
        ('electricity', 'Electricity Fault'),
        ('waste', 'Waste Collection'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('logged', 'Logged with Municipality'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    photo = models.ImageField(upload_to='reports/%Y/%m/%d/', blank=True, null=True)
    location_lat = models.FloatField(blank=True, null=True)
    location_lng = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reference_number = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.reference_number:
            import random
            self.reference_number = f"RPT-{random.randint(10000, 99999)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_number} - {self.category}"
    



    