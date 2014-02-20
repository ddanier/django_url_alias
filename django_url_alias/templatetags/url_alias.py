from django import template
from django.template.defaulttags import url as vanilla_url
from ..utils import reverse_rewrite


register = template.Library()


class AliasedURLNode(template.Node):
    def __init__(self, url_node):
        self.asvar = url_node.asvar
        url_node.asvar = None  # we need to handle pushing into context ourself, so we skip the URLNode mechanism
        self.url_node = url_node

    def render(self, context):
        url = self.url_node.render(context)
        url = reverse_rewrite(url)

        if self.asvar:
            context[self.asvar] = url
            return ''
        else:
            return url


@register.tag
def url(parser, token):
    return AliasedURLNode(vanilla_url(parser, token))
