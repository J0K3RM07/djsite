from django import template
from uptrade.models import *
register = template.Library()

@register.inclusion_tag('uptrade/custom.html')
def draw_menu():
    menu = MainMenu.objects.all()
    return {'menu': menu}