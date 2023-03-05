from django import template
from django.template import loader
from django.urls import reverse

from menu.models import HeadMenu

register = template.Library()


def find_url(url, obj, path):
    obj_url = reverse(obj.named_url) if obj.named_url else obj.url
    if obj_url == url:
        return path
    for child in obj.childes.all():
        res = find_url(url, child, path + ' ' + str(child.id))
        if res:
            return res


def create_menu(obj, path, current_point):
    childes_obj = obj.childes.all()
    temp_link = loader.get_template('link.html')
    parent = temp_link.render({'obj': obj})
    childes = []
    next_point = None if len(path) == current_point + 1 else current_point + 1
    for child in childes_obj:
        if next_point and path[next_point] == child.id:
            childes.append(create_menu(child, path, next_point))
        else:
            childes.append(temp_link.render({'obj': child}))
    temp_menu = loader.get_template('menu.html')
    return temp_menu.render({'parent': parent, 'childes': childes})


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_title):
    try:
        head = HeadMenu.objects.get(title=menu_title)
    except HeadMenu.DoesNotExist:
        return f'Menu "{menu_title}" not found'

    current_url = context.request.path

    try:
        find_path = list(map(
            int,
            find_url(current_url, head.menu, str(head.menu.id)).split())
        )
    except AttributeError:
        temp_link = loader.get_template('link.html')
        return temp_link.render({'obj': head.menu})

    return create_menu(head.menu, find_path, 0)
