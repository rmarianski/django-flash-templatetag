"""
template tag that gives access to the flash messages
as well as removing them
"""

from django import template

class FlashMessagesNode(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name
    def render(self, context):
        # assume that we can access the request
        request = context['request']
        flash_messages = dict(request.flash.items())
        request.flash.clear()
        context[self.var_name] = flash_messages
        return ''

def do_flash_messages(parser, token):
    try:
        # Splitting by None == splitting by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        var_name = 'flash_messages'
    else:
        try:
            as_, var_name = arg.split()
        except ValueError:
            raise template.TemplateSyntaxError, "%r tag requires 'as var_name' syntax" % token.contents.split()[0]
    return FlashMessagesNode(var_name)

register = template.Library()
register.tag('get_and_remove_flash_messages', do_flash_messages)
