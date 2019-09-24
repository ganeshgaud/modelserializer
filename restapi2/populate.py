import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','restapi2.settings')
import django
django.setup()


from testapp.models import Student
from faker import Faker
from random import *
faker=Faker()
def populate(n):
    for i in range(n):
        srno=randint(100,999)
        sname=faker.name()
        saddr=faker.city()
        # smarks=choice([,60000,1000,55000,43000,25000])
        smarks=randint(50,99)
        emp_record=Student.objects.get_or_create(srno=srno,sname=sname,saddr=saddr,smarks=smarks)

populate(5)
