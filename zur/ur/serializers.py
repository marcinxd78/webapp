from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Tag, Department, Priority, Work_cat, Fix_cat


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name_dep',)

class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = ('type_prior',)

class Work_catSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work_cat
        fields = ('name_work_cat',)

class Fix_catSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fix_cat
        fields = ('name_fix_cat',)

class TagSerializer(serializers.ModelSerializer):
    depart = DepartmentSerializer()
    priority = PrioritySerializer()
    work_cat = Work_catSerializer()
    fix_dep = Fix_catSerializer()
    class Meta:
        model = Tag
        fields = ('id', 'number', 'depart', 'machine', 'add_date', 'expiry_date', 'priority', 'explain', 'work_cat',
                  'fix_dep', 'is_done', 'fix_date',)

