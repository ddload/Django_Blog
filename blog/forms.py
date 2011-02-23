from django import forms
from django.forms.models import ModelForm

from Django_Blog.blog.models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField()

    def clean_message(self):
        message = self.cleaned_data.get('message', '')
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message

