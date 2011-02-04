from django.forms import ModelForm

from Django_Blog.blog.models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        
        
