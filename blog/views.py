# Django Imports
from django.shortcuts import render_to_response
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Project Imports
from Django_Blog.blog.models import Entry
from Django_Blog.blog.forms import EntryForm


class BlogIndex(ListView):
    """
        Is a subclass of ``ListView`` and is a class based generci view.
        Pagination is currently setup for 10 entries per page.
    """
    
    context_object_name='blog_index'
    template_name='blog/index.html'
    paginate_by = 10
    paginator_class = Paginator
    
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Entry.objects.all().order_by('created')
        else:
            return Entry.objects.published().order_by('created')
        
@login_required
def blog_editor(request, slug=None):
    form = EntryForm(request.POST or None,
                     instance=slug and Entry.objects.get(slug=slug))
    # Save new/edited entry
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('blog_index'))
    
    return render_to_response('blog/editor.html',
                              {'form':form},
                              context_instance=RequestContext(request))

@login_required
def blog_delete(request, slug):
    entry = Entry.objects.get(slug=slug)
    entry.delete()
    return HttpResponseRedirect(reverse('blog_index'))
