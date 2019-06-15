from django.views.generic import View
from django.http import JsonResponse

from celery_tasks.appone.tasks import add
from celery_tasks.apptwo.tasks import mult
from celery_tasks.appthree.tasks import comment


class One_View(View):
    def get(self, request):
        add.delay(5, 5)
        return JsonResponse({'result': 'ok'})


class Two_View(View):
    def get(self, request):
        mult.delay(5, 5)
        return JsonResponse({'result': 'ok'})


class Three_View(View):
    def get(self, request):
        comment.delay(5, 5)
        return JsonResponse({'result': 'ok'})
