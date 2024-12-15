from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import random

def home(request):
    return HttpResponse('Hello, World!')

# {
#     'Status': True,
#     'data': [
#         {}
#     ]
# }

def get_quiz(request):
    try:
        question_objs = list(Question.objects.all())
        random.shuffle(question_objs)
        data = []
        for question_obj in question_objs:
            data.append({
                "category": question_obj.category.category_name,
                "question": question_obj.question,
                "marks": question_obj.marks,
                "answer": question_obj.ger_answer()
            })
        payload = {"status" :True , "data" : data}
        return JsonResponse(payload)
    except Exception as e:
        return HttpResponse(str(e))
        print(e)

    return HttpResponse('someting went wrong')
    

    