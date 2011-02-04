from Django_Blog.blog.models import Entry

def blog_index(request):
    entries = Entry.objects.all()
    return render_to_response('blog/index.html', {'entries': entries})
