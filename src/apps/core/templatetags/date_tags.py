from datetime import datetime

from django.template import Library

register = Library()

@register.simple_tag(name='current_time')
def current_time(date_start):
    data = date_start.split('/')
    br_data = f'{data[1]}/{data[0]}/{data[2]}'
    ajusted_data = datetime.strptime(br_data, "%d/%m/%y")
    
    return ajusted_data.strftime("%d/%m/%Y")