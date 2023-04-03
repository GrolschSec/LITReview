from django.contrib import admin
from ticket.models import Review, Ticket
from authentication.models import CustomUser

admin.site.register(Review)
admin.site.register(Ticket)
admin.site.register(CustomUser)
