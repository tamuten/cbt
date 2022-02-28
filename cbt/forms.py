from cProfile import label
from django import forms
from .models import Thought


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class WorkForm(forms.ModelForm):
    moody = forms.CharField(widget=forms.Textarea,label='モヤモヤ')
    event = forms.CharField(widget=forms.Textarea,label='出来事')
    old_think = forms.CharField(widget=forms.Textarea,label='考えたこと')
    basis = forms.CharField(widget=forms.Textarea,label='根拠')
    counter_evidence = forms.CharField(widget=forms.Textarea,label='反証')
    class Meta:
        model = Thought
        fields = ('__all__')
        labels = {
            'pub_datetime': '',
        }
