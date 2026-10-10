from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from students.models import student
from .serializers import studentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET","POST"])
def studentsViews(request):
   if request.method == "GET":
      studentss = student.objects.all()
      serializer = studentSerializer(studentss, many = True  )
      return Response (serializer.data , status=status.HTTP_200_OK )

   if request.method == "POST":
      serializer = studentSerializer(data =request.data )
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def studentsDetailsViews(request,pk):

   try:
      
      studentss = student.objects.get(pk=pk)

   except studentss.DoesNotExist:
       
       
       return Response( status=status.HTTP_404_NOT_FOUND)

   if request.method == "GET":
      serializer = studentSerializer(studentss)
      return Response (serializer.data, status=status.HTTP_200_OK)

   elif request.method == "PUT":
      serializer = studentSerializer(studentss, data = request.data)

      if serializer.is_valid():
         serializer.save()

         return Response(serializer.data, status=status.HTTP_200_OK)

      return Response(tatus=status.HTTP_404_NOT_FOUND)

   elif request.method == "DELETE":
      studentss.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
   
     


      