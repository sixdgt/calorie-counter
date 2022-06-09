from pyexpat import model
from django.db import models

# Create your models here.
class AppUser(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.IntegerField(max_length=11)
    gender = models.CharField(max_length=10)
    dob = models.DateField(default=0)
    blood_group = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    verification_code = models.CharField(max_length=8)
    is_verified = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=0)
    updated_at = models.DateTimeField(null=True)
    removed_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "app_users"

class HealthStatus(models.Model):
    user = models.BigIntegerField(max_length=20)
    health_issue = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    is_removed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=0)
    updated_at = models.DateTimeField(null=True)
    removed_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "app_health_status"

class Diet(models.Model):
    health_status = models.BigIntegerField(max_length=20)
    diet_title = models.CharField(max_length=100)
    diet_plan = models.TextField(max_length=500)
    diet_duration = models.CharField(max_length=200)
    medicine_details = models.TextField(max_length=500)
    remarks = models.TextField(max_length=500)
    is_removed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=0)
    updated_at = models.DateTimeField(null=True)
    removed_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "app_diet"
