from django import template

from django.db.models import Max


register = template.Library()

@register.filter
def get_max_lbs(value):
    """Gets the max weight from the iterable"""
    return value.set_set.all().aggregate(Max('weight_in_lbs'))['weight_in_lbs__max']


@register.filter
def add_class(field, css):
    """Adds a class onto specifically a form tag"""
    return field.as_widget(attrs={"class": css})