import django.forms

from . import models


class CreatePollForm(django.forms.Form):
    question = django.forms.CharField(label='Question', min_length=10, widget=django.forms.Textarea, required=True)
    option_1 = django.forms.CharField(label='Option one', required=True)
    option_2 = django.forms.CharField(label='Option two', required=True)
    option_3 = django.forms.CharField(label='Option three',required=False)
    option_4 = django.forms.CharField(label='Option four',required=False)

    def clean_question(self):
        value = self.data['question']
        if models.Poll.objects.filter(question__iexact=value).exists():
            self.add_error('question', 'Question should be unique.')
        return value