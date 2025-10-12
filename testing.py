from models.models import *


data = Depend_Resources()

a = data.getall()

for i in a:
    print(i)