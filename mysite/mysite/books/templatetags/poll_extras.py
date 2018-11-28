from django import template
import datetime

register=template.Library()

#自定义模板过滤器
@register.filter(name='cut')
def cut(value,arg):
    return value.replace(arg,'')


@register.filter
def lower(value):
    return value.lower()

#编译模板标签
@register.tag(name='current_time')
def do_current_time(parser,token):
    try:
        tag_name,format_string=token.split_contents()
    except ValueError:
        msg='%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode(format_string[1:-1])#去掉模板标签开头和结尾的引号

class CurrentTimeNode(template.Node):
    def __init__(self,format_string):
        self.format_string=str(format_string)

    def render(self,context):
        now=datetime.datetime.now()
        return now.strftime(self.format_string)
