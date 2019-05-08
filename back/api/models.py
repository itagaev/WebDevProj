from django.db import models
from django.contrib.auth.models import User
import datetime

class TaskList(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_jason(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Hospital(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    description = models.TextField()
    place = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'description': self.description,
            'place': self.place,
            'address': self.address
        }

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'mobile': self.mobile,
            'address': self.address
        }

class Patient(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'mobile': self.mobile,
            'address': self.address
        }

class Medicine(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    cost = models.IntegerField()
    type = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'company': self.company,
            'cost': self.cost,
            'type': self.type,
            'description': self.description,
        }

class Appointment(models.Model):
    type = models.CharField(max_length=100)
    # date = models.DateTimeField(datetime.datetime.now())
    description = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.type)

    def to_json(self):
        return {
            'id': self.id,
            # 'date': self.date,
            'description': self.description,
            'patient': self.patient.to_json(),
            'doctor': self.doctor.to_json()
        }



class Task(models.Model):
    name=models.CharField(max_length=50)
    created_at=models.DateTimeField(datetime.datetime.now())
    due_on=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=200)
    task_list=models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.name, self.created_at,self.due_on,self.status)

    def to_json(self):
        return {
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status,
            'task_list': self.task_list.to_json(),
        }