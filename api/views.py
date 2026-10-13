from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from students.models import student
from employees.models import employee
from .serializers import studentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import employeeSerializer
from django.http import Http404
from rest_framework import mixins , generics


''''
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
   
     
class Employee(APIView):

   def get(self,request):
      employees = employee.objects.all()
      serializer = employeeSerializer(employees , many = True)
      return Response (serializer.data , status=status.HTTP_200_OK)

   def post(self,request):
      serializer = employeeSerializer( data = request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data , status=status.HTTP_201_CREATED)
      return Response(serializer.error , status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetails(APIView):

   def get_object(self,pk):

      try:
         return employee.objects.get(pk=pk)
      except:
         return Http404


   def get (self,request,pk):

      employee = self.get_object(pk)
      serializer = employeeSerializer(employee)
      return Response(serializer.data , status=status.HTTP_200_OK)

   def put(self,request,pk):
      employee = self.get_object(pk)
      serializer = employeeSerializer(employee,data = request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_200_OK)
      return Response(serializer.errors)

   def delete (self,request,pk):
      employee = self.get_object(pk)
      employee.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

''' 


#mixins

class Employee(mixins.ListModelMixin, generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer

    def get(self , request):
        return self.list(request)

    def post (self, request):
        return self.create(request)

class EmployeeDetails( generics.RetrieveUpdateDestroyAPIView , ):
    
     queryset = employee.objects.all()
     serializer_class = employeeSerializer

     def get( self, request ,pk):
         
         return self.retrieve(request,pk)

     def put(self,request,pk,):
          return self.update(request,pk)

     def delete(self,request,pk):
         return self.destroy(request , pk)