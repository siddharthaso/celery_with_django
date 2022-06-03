# from celery.decorators import task
# @task(name = "sum_two_numbers")
# def add(x,y):
#     return x+y

from celery import shared_task

# from django.utils import timezone
# timezone.now()

@shared_task(bind = True)
def test_func(self):
    #operations
    for i in range(10):
        print(i)
    print(10/0)
    return r"Done"""


#tasks.py

from celery import Celery
BROKER_URL = 'redis://localhost:6379/0'
celery_app = Celery('Restaurant', broker=BROKER_URL)

# Functions which are decorated with @celery_app.task considered celery tasks.
@celery_app.task
def cooking_task(table_no, dishes):
    print("Started cooking for Table Number : "+table_no)
    for dish in dishes:
        print("Cooking : "+dish)
    print("Done cooking for Table Number : "+table_no)


# celery -A tasks worker --pool=solo --loglevel=info
