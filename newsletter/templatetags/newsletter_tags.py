from django import template
from newsletter.forms import SubscribeForm

register = template.Library()

@register.inclusion_tag("newsletter/subscribe.html", takes_context=True)
def newsletter_subscribe(context):
    context["form"] = context.get("subscribe_form", SubscribeForm())
    return context