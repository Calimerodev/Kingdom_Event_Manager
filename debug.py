from models.models import *
from models.data_filter import *

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


#Resources().insert("Ballesta", 12 , "FALSE" , "Kingdom" )
a = Resources().getall()
print(a)