from django import forms
from .models import FeelChoices


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class WorkForm(forms.Form):
    feel_val = [
        ('sad', '悲しい'),
        ('mad', '怒り'),
        ('funny', '楽しい'),
        ('love', '愛情')
    ]

    pub_datetime = forms.DateTimeField()
    feeling = forms.ChoiceField(choices=feel_val)
    moody = forms.CharField(max_length=400, widget=forms.Textarea)
    event = forms.CharField(max_length=100, widget=forms.Textarea)
    old_think = forms.CharField(max_length=400, widget=forms.Textarea)
