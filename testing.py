from models import models


def clear():
    a = models.Events().getall()

    for e in a:
        print(e)


models.Depend_Resources().create()
models.Incompatibles_Resources().create()
models.Resources().create()

