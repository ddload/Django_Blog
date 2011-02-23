# Django Imports
from django.shortcuts import render_to_response
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

# Project Imports
from Django_Blog.blog.models import Entry
from Django_Blog.blog.forms import EntryForm, ContactForm


class BlogIndex(ListView):
    """
        Is a subclass of ``ListView`` and is a class based generic view,
        which shows a listing of all entries (based on whether a user is
        logged in or not).
        Pagination is currently setup for 10 entries per page.
    """
    
    context_object_name='blog_index'
    template_name='blog/index.html'
    paginate_by = 3
    paginator_class = Paginator
    
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Entry.objects.all().order_by('created')
        else:
            return Entry.objects.published().order_by('created')
        
@login_required
def blog_editor(request, slug=None):
    """
        ``ModelForm`` view that is used for adding/editing blog
        entries.
    """
    form = EntryForm(request.POST or None,
                     instance=slug and Entry.objects.get(slug=slug))
    # Save new/edited entry
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('blog_index'))
    
    return render_to_response('blog/editor.html',
                              {'form':form},
                              context_instance=RequestContext(request))

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data.get('sender', 'bmheight@gmail.com')
            send_mail(
                'Feedback from your site, topic: %s' % subject,
                message, sender,
                ['lasko@djangoblog.net']
            )
            return HttpResponseRedirect(reverse('blog_index'))
    else:
        form = ContactForm()
    return render_to_response('contact.html', {'form': form})
                                                                            
