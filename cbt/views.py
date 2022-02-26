from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from .models import Thought
from .forms import NameForm, WorkForm


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
