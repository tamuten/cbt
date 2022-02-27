from django import forms
from .models import Thought


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class WorkForm(forms.ModelForm):
    # feel_val = [
    #     ('sad', '悲しい'),
    #     ('mad', '怒り'),
    #     ('funny', '楽しい'),
    #     ('love', '愛情')
    # ]

    # pub_datetime = forms.DateTimeField()
    # feeling = forms.ChoiceField(choices=feel_val)
    # moody = forms.CharField(max_length=400, widget=forms.Textarea)
    # event = forms.CharField(max_length=100, widget=forms.Textarea)
    # old_think = forms.CharField(max_length=400, widget=forms.Textarea)
    moody = forms.CharField(widget=forms.Textarea)
    event = forms.CharField(widget=forms.Textarea)
    old_think = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Thought
        fields = ('pub_datetime', 'moody', 'event', 'old_think')
