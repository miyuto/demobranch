from django import template
from home.models import *

register = template.Library()

@register.filter
def getChilds(parentId):
    return TblCategory.objects.filter(cate_parent_id=parentId)

@register.filter
def hasChilds(parentId):
    childs = TblCategory.objects.filter(cate_parent_id=parentId)
    if(childs is not None):
        if(len(childs) > 0):
            return "True"
        return "False"