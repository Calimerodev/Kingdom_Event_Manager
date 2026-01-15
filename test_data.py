from models.data_filter import *
from models.models import *

"""
a =  Manager_Events().insert_event(
                        "uwu",
                        "lighthouse",
                        0,
                        'FALSE',
                        '1/1/2025',
                       '2/1/20250',
                       )

"""

#Events().delete_id(2)
a = Manager_Events().filter(place="ligouse")
print(a)
