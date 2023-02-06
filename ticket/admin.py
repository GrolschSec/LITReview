from django.contrib import admin
from ticket.models import Review, Ticket, UserFollows
from django.contrib.auth.models import User

admin.site.register(Review)
admin.site.register(Ticket)
admin.site.register(UserFollows)

