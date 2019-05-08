from rest_framework import serializers
from api.models import Task, TaskList, Hospital, Doctor, Patient, Appointment, Medicine
from django.contrib.auth.models import User

import datetime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class TaskListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    created_by = UserSerializer()

    class Meta:
        model = TaskList
        fields = ('id', 'name', 'created_by',)

class HospitalSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    type = serializers.CharField()
    description = serializers.CharField()
    place = serializers.CharField()
    address = serializers.CharField()

    class Meta:
        model = Hospital
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    mobile = serializers.CharField()
    address = serializers.CharField()

    class Meta:
        model = Doctor
        fields = '__all__'


class PatienSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    mobile = serializers.CharField()
    address = serializers.CharField()

    class Meta:
        model = Patient
        fields = '__all__'

class MedicineSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    company = serializers.CharField()
    cost = serializers.IntegerField()
    type = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Medicine
        fields = '__all__'

class AppointmentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    type = serializers.CharField()
    description = serializers.CharField()
    patient = PatienSerializer()
    doctor = DoctorSerializer()

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    #created_at = serializers.DatetimeField()
    #due_on = serializers.DatetimeField()
    status=serializers.CharField()
    tasklist=TaskListSerializer()

