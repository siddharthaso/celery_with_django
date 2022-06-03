from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func, cooking_task

# Create your views here.
def test(request):
    test_func.delay()

    # Dishes ordered for Table-1
    table_1_dishes = ["khamman", "Thepala", "Samosha","Pani-Puri"]
    # Call the cooking_task.delay task with input parameters defined for that Task.
    result = cooking_task.delay("Table-1", table_1_dishes)
    # prints the task id
    print(result)       

    table_2_dishes = ["Manchuriyam", "noodles"]
    result2 = cooking_task.apply_async(args=["Table-2", table_2_dishes])
    print(result2)

    table_3_dishes = ["Butter Naan", "Panjabi"]
    result3 = cooking_task.apply_async(args=["Table-3", table_3_dishes])
    print(result3)

    table_4_dishes = ["rose","sunflower"]
    result4 = cooking_task.apply_async(args=["Table-4", table_4_dishes])
    print(result4)

    return HttpResponse("<h1>Done</h1>")
