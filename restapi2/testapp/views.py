from django.shortcuts import render
from django.views import View
import io
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializers
from .models import Student
# Create your views here.
class StudentCrud(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id')
        if id is not None:
            emp=Student.objects.get(id=id)
            print(emp)
            serializer=StudentSerializers(emp)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        emp=Student.objects.all()
        print(emp)
        serializer=StudentSerializers(emp,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    def put(self.request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(json_data)
        id=pdata.get('id')
        std=Student.objects.get(id=id)
        serializer=StudentSerializers(std,data=pdata)
        if serializer.is_valid():
            serializer.save()
            json_data=JSONRenderer().render('Student Data Updated Successfully!!!')
