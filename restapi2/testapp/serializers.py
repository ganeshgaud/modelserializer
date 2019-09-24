from .models import Student
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    # srno=serializers.IntegerField()
    # sname=serializers.CharField(max_length=64)
    # saddr=serializers.CharField(max_length=64)
    # smarks=serializers.IntegerField()
    class Meta:
        model=Student
        fields='__all__'
