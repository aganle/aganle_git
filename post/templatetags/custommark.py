"""自定义过滤器"""
from django import template
import markdown

register = template.Library()
@register.filter
def mark(value):
    """将内容转换为markdown格式"""
    return markdown.markdown(value)