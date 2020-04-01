from django.template import Library

from apps.utils.date_adjustment import date_adjustment

register = Library()

@register.simple_tag(name='current_time')
def current_time(date_start):
    return date_adjustment(date_start)