from django import template
from notes.models import Notes
register=template.Library()
from django.utils.safestring import mark_safe



@register.filter(name='tagmark')
def tagmark(notebook,query):
    return mark_safe(notebook.replace(query,"<mark>"+query+"</mark>"))



@register.filter(name='countnotes')
def countnotes(notebook,email):
    return Notes.return_count_by_name(email,notebook)


@register.filter(name='abs_value')
def abs_value(value):
    try:
        return abs(value)
    except:
        return None