from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from .forms import NameForm, WorkForm
import json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = NameForm()

    return render(request, 'cbt/name.html', {'form': form})


def work(request):
    form = WorkForm(initial={
        'pub_datetime': timezone.now()
    })
    return render(request, 'cbt/work.html', {'form': form})

def user(request):
    return render(request, 'cbt/user.html')

def get_user(request):
    params = [
        {
            "id": 1,
            "name": "Takuya Tejima",
            "description": "東南アジアで働くエンジニアです。"
        },
        {
            "id": 2,
            "name": "Yohei Noda",
            "description": "アウトドア・フットサルが趣味のエンジニアです。"
        },
        {
            "id": 3,
            "name": "Takashi Tamura",
            "description": "東大宮在住"
        }
    ]
    json_str = json.dumps(params, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)

