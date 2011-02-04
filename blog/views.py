from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from Django_Blog.blog.models import Entry
from Django_Blog.blog.forms import EntryForm

def blog_index(request):
    entries = Entry.objects.all()
    return render_to_response('blog/index.html', {'entries': entries})

def blog_editor(request, id=None):
    form = EntryForm(request.POST or None,
                     instance=id and Entry.objects.get(id=id))
    # Save new/edited entry
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('blog_index'))
    
    return render_to_response('blog/editor.html', {'form':form})

def blog_delete(request, id):
    entry = Entry.objects.get(id=id)
    entry.delete()
    return HttpResponseRedirect(reverse('blog_index'))

class BlogView(TemplateView):
    template_name='blog/view.html'


        
        
