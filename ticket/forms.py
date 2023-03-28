from django.forms import Form, ModelForm, ModelChoiceField, HiddenInput, formset_factory
from .models import Ticket, Review


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            "headline",
            "rating",
            "body",
        ]
