from django import template
from django.utils.html import escape


register = template.Library()


@register.simple_tag
def custom_meta(attr, name, content):
    """
    Generates a custom meta tag:
    <meta {attr}="{name}" content="{content}">
    :param attr: meta attribute name
    :param name: meta name
    :param content: content value
    """
    return '<meta {attr}="{name}" content="{content}">'.format(
        attr=escape(attr), name=escape(name), content=escape(content)
    )


@register.simple_tag
def meta(name, content):
    """
    Generates a meta tag according to the following markup:
    <meta name="{name}" content="{content}">
    :param name: meta name
    :param content: content value
    """
    return custom_meta('name', name, content)


@register.simple_tag
def meta_list(name, lst):
    """
    Renders in a single meta a list of values (e.g.: keywords list)
    :param name: meta name
    :param lst: values
    """
    try:
        return custom_meta('name', name, ', '.join(lst.split()))
    except Exception:
        return ''


@register.simple_tag
def title_prop(value):
    """
    Title tag
    :param value: title value
    """
    return '<title>%s</title>' % escape(value)


@register.simple_tag(takes_context=True)
def meta_namespaces(context):
    """
    Include OG namespaces. To be used in the <head> tag.
    """
    # do nothing if meta is not in context
    if not context.get('meta'):
        return ''

    meta = context['meta']
    namespaces = ['og: http://ogp.me/ns#']

    # add Facebook namespace
    if meta.use_facebook:
        namespaces.append('fb: http://ogp.me/ns/fb#')

    # add custom namespaces
    # needs to be after Facebook
    if meta.custom_namespace:
        custom_namespaces = meta.custom_namespace
        if isinstance(meta.custom_namespace, string_types):
            custom_namespaces = [meta.custom_namespace]
        for ns in custom_namespaces:
            custom_namespace = '{0}: http://ogp.me/ns/{0}#'.format(ns)
            namespaces.append(custom_namespace)

    return mark_safe(' prefix="{0}"'.format(' '.join(namespaces)))
