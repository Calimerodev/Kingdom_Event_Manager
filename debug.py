import data_filter
from models.models import *
from data_filter import *


def init_data_base():
    Events().create()
    Resources().create()
    Events_Resources_Relation().create()
    Incompatibles_Resources().create()
    Depend_Resources().create()



a = Events().getall()

for i in a:
    Events().delete_id(id_event=i[0])

print(Events().getall())