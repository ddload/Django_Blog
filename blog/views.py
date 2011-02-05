# Django Imports
from django.shortcuts import render_to_response
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

# Project Imports
from Django_Blog.blog.models import Entry
from Django_Blog.blog.forms import EntryForm

@login_required
def blog_editor(request, id=None):
    form = EntryForm(request.POST or None,
                     instance=id and Entry.objects.get(id=id))
    # Save new/edited entry
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('blog_index'))
    
    return render_to_response('blog/editor.html',
                              {'form':form},
                              context_instance=RequestContext(request))

@login_required
def blog_delete(request, id):
    entry = Entry.objects.get(id=id)
    entry.delete()
    return HttpResponseRedirect(reverse('blog_index'))
