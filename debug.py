import data_filter
from models.models import *
from data_filter import *

def clean():
    datas = Events().getall()
    for data in datas:
        Events().delete_id(data[0])


def init_data_base():
    Events().create()
    Resources().create()
    Events_Resources_Relation().create()
    Incompatibles_Resources().create()
    Depend_Resources().create()


#a = Manager_Events().show_resouce_event()

#Manager_Events().insert_event("minar y cobrar impuesto","Kingdom",-1,"FALSE","12/10","13/10", [1,3])

#clean()

#a = Events_Resources_Relation().getall()

a = Events_Resources_Relation().getall()
#a = Depend_Resources().getall()

for i in a:
    print(i)


