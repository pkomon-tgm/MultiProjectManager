from django import template

register = template.Library()


@register.filter
def label_with_class(field, arg):
    return field.label_tag(attrs={"class": arg})


@register.filter
def field_with_class(field, arg):
    return field.as_widget(attrs={"class": arg})
