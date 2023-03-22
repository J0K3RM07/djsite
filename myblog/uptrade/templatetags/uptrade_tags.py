from django import template
from uptrade.models import *
register = template.Library()

@register.inclusion_tag('uptrade/custom.html')
def draw_menu(name):
    menu = MainMenu.objects.all()
    return {'menu': menu, 'name':name}