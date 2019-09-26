from django.shortcuts import render
from django.views import View
import io
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializers
from .models import Student
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StudentCrud(View):
    def is_id_valid(self,id):
        try:
            std=Student.objects.get(id=id)
        except ObjectDoesNotExist:
            std=None
        return std
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

    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id')
        std=Student.objects.get(id=id)
        serializer=StudentSerializers(std,data=pdata,partial=True)
        if serializer.is_valid():
            serializer.save()
            json_data=JSONRenderer().render('Student Data Updated Successfully!!!')
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')


    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        serializer=StudentSerializers(data=pdata)
        if serializer.is_valid():
            serializer.save()
            json_data=JSONRenderer().render('Student Data Added Successfully!!!')
            return HttpResponse(json_data,content_type='application/json')

    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id')
        std=self.is_id_valid(id)
        if std is None:
            json_data=JSONRenderer().render('Student record not found')
            return HttpResponse(json_data,content_type='application/json')
        std.delete()
        json_data=JSONRenderer().render('Student Data deleted Successfully!!!')
        return HttpResponse(json_data,content_type='application/json')
