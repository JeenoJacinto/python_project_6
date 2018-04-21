from django import template
from django.utils.safestring import mark_safe
import markdown2

from mineral_data.models import Mineral

register = template.Library() # this will help register our tags


@register.filter('list_item_by_index')
def list_item_by_index(data, idx):
    """converts dict into tuple"""
    fmt_data = data[idx]
    return fmt_data


@register.filter('get_items')
def get_items(data):
    """converts dict into tuple"""
    fmt_data = data.items()
    return fmt_data


@register.filter('formula')
def formula(data):
    """adds <td class="mineral__formula"></td>"""
    fmt_data = '<td class="mineral__formula">' + data + '</td>'
    return fmt_data


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    """Converts markdown text to HTML"""
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)
