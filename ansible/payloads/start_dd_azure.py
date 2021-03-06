import os
from mongoengine import *
import socket
import sys


db_con_string = sys.argv[4]
con = connect(host=db_con_string)
storage_accnt = sys.argv[1]
access_key = sys.argv[2]
container = sys.argv[3]
project = sys.argv[5]


hostname = socket.gethostname()

class Discover(Document):
    host = StringField(required=True, max_length=200 )
    ip = StringField(required=True)
    subnet = StringField(required=True, max_length=50)
    network = StringField(required=True, max_length=50)
    ports = ListField()
    cores = StringField(max_length=2)
    cpu_model = StringField(required=True, max_length=150)
    ram = StringField(required=True, max_length=50)
    disk = StringField(required=True, max_length=50)
    project = StringField(required=True, max_length=50)
    meta = {
        'indexes': [
            {'fields': ('host', 'project'), 'unique': True}
        ]
    }


class BluePrint(Document):
    host = StringField(required=True, max_length=200)
    ip = StringField(required=True)
    subnet = StringField(required=True, max_length=50)
    network = StringField(required=True, max_length=50)
    ports = ListField()
    cores = StringField(max_length=2)
    cpu_model = StringField(required=True, max_length=150)
    ram = StringField(required=True, max_length=50)
    machine_type = StringField(required=True, max_length=150)
    status = StringField(required=False, max_length=100)
    image_id = StringField(required=False, max_length=100)
    vpc_id = StringField(required=False, max_length=100)
    subnet_id = StringField(required=False, max_length=200)
    public_route = BooleanField(required=False)
    ig_id = StringField(required=False, max_length=100)
    route_table = StringField(required=False, max_length=100)
    vm_id = StringField(required=False, max_length=200)
    project = StringField(required=True, max_length=50)
    nic_id = StringField(max_length=200)
    meta = {
        'indexes': [
            {'fields': ('host', 'project'), 'unique': True}
        ]
    }
    
osdisk = Discover.objects(host=hostname,project=project)[0]['disk']
BluePrint.objects(host=hostname,project=project).update(status='10')
os.system('sudo dd if='+osdisk+' bs=1M status=progress | azbak - /'+container+'/'+hostname+'.raw --storage-account '+storage_accnt+' --access-key '+access_key)

BluePrint.objects(host=hostname, project=project).update(status='25')
con.close()
