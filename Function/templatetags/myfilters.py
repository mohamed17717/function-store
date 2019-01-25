from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def replacetabs(value):
    value = value.replace('\t', '    ')
    value = value.replace(' ', '&nbsp;')
    return value

@register.filter
@stringfilter
def split(value, delemeter):
    return value.split(delemeter)

@register.filter
@stringfilter
def replacelines(value):
    return value.replace('\n', '<br />')