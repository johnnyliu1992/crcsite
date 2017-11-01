from django import template

register = template.Library()

@register.filter
def getvalue(value, arg):
    """get vaule of a hash by key arg """
    value=value[arg]
    return value
