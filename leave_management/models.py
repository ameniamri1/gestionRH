from django.contrib.auth.models import User
from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Ajout du champ user
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ], null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    photo_url = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Leave(models.Model):
    LEAVE_TYPES = [
        ('Vacation', 'Congé payé'),
        ('Sick leave', 'Congé maladie'),
        ('Parental leave', 'Congé parental'),
        ('Other', 'Autre'),
    ]

    APPROVAL_STATUSES = [
        ('Pending', 'En attente'),
        ('Approved', 'Approuvé'),
        ('Rejected', 'Refusé'),
    ]

    leave_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=APPROVAL_STATUSES, default='Pending')
    manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_leaves')

    def __str__(self):
        return f"{self.leave_type} from {self.start_date} to {self.end_date} by {self.employee}"
