import json
import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'

def get_resource(id=None):
    d={}
    d={
    'id':id,
    }
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(d))
    # print(resp.status_code)
    if id is None:
        data=resp.json()
        for i in data:
            print("**********************************************")
            for k,v in i.items():
                print(k,"==",v)
    else:
        print("**********************************************")
        data=resp.json()
        for k,v in data.items():
            print(k,"==",v)
        print("**********************************************")
# get_resource(1)

def put_resource(id):
    d={
    'id':id,
    'sname':'Pranav',
    'saddr':'Hyderabad'
    }
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(d))
    print(resp.status_code)
    print(resp.json())

put_resource(5)
