from django import template
from ticket.models import Ticket

register = template.Library()


@register.filter
def is_ticket(obj):
    return isinstance(obj, Ticket)
