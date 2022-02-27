from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django import forms

from .models import Feeling, NewThinking, Thought

from .forms import NameForm, WorkForm
import json

NewThinkFormSet = forms.inlineformset_factory(
        parent_model=Thought,
        model=NewThinking,
        fields=('new_think',),
        extra=1,
)
FeelFormSet = forms.inlineformset_factory(
        parent_model=Thought,
        model=Feeling,
        fields=('feel_variation',),
        extra=2,
)


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
    work = Thought()

    work_form = WorkForm(instance=work, initial={
        'pub_datetime': timezone.now()})
    new_think_formset = NewThinkFormSet(
        instance=work,
    )
    feeling_formset = FeelFormSet(
        instance=work,
    )
    return render(request, 'cbt/work.html', {'form': work_form, 'new_think_formset': new_think_formset, 'feeling_formset': feeling_formset})


def save_work(request):
    work_form = WorkForm(request.POST or None)
    context = {'form': work_form}
    if request.method == 'POST' and work_form.is_valid():
        post = work_form.save(commit=False)
        new_think_formset = NewThinkFormSet(request.POST, instance=post)
        feeling_formset = FeelFormSet(request.POST, instance=post)
        if new_think_formset.is_valid() and feeling_formset.is_valid():
            post.save()
            new_think_formset.save()
            feeling_formset.save()
            return HttpResponseRedirect('/cbt/')
        else:
            context['new_think_formset'] = new_think_formset
            context['feeling_formset'] = feeling_formset

    else:
        context['new_think_formset'] = NewThinkFormSet()
        context['feeling_formset'] = FeelFormSet()
    
    return render(request, 'cbt/work.html', context)


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
