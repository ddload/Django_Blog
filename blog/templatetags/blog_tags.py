from django import template
from django.db.models import get_model

from pygments import highlight
from pygments.lexers import guess_lexer, PythonLexer
from pygments.formatters import HtmlFormatter
from BeautifulSoup import BeautifulSoup

register = template.Library()

@register.filter(name='render')
def render(value):
    try:
        soup = BeautifulSoup(value)
        code_blocks = soup.findAll('code')
        for code in code_blocks:
            try:
                lexer = guess_lexer(code.string)
            except ValueError:
                lexer = PythonLexer()
            code.replaceWith(highlight(code.string, lexer, HtmlFormatter()))
        return str(soup)
    except:
        return value

###########################
    
"""
Template tag name: get_latest
usage:
    {% get_latest weblog.Link 5 as recent_links %}
    {% get_latest weblog.Entry 10 as latest_entries %}
    {% get_latest comments.Comment 5 as recent_comments %}
"""
class LatestContentNode(template.Node):
    def __init__(self, model, num, varname):
        self.num, self.varname = num, varname
        self.model = get_model(*model.split('.'))

    def render(self, context):
        context[self.varname] = self.model._default_manager.all().order_by('-created')[:self.num]
        return ''

def get_latest(parser, token):
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError, "get_latest tag takes exactly four arguments"
    if bits[3] != 'as':
        raise TemplateSyntaxError, "third argument to get_latest tag must be 'as'"
    return LatestContentNode(bits[1], bits[2], bits[4])

get_latest = register.tag(get_latest)
                
###########################
        
@register.simple_tag
def active(request, pattern):
    if request.path.startswith(pattern):
        return 'active'
    return ''
