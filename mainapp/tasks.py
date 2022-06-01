from celery import shared_task

# from django.utils import timezone
# timezone.now()

@shared_task(bind = True)
def test_func(self):
    #operations
    for i in range(10):
        print(i)
    return r"Done"""

