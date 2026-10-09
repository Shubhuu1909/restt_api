from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from students.models import student


# Create your views here.

def studentsViews(request):
    students = student.objects.all()
    Student_list = list(students.values())
    return JsonResponse(Student_list, safe=False)

