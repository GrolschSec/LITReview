from django.forms import Form, ModelForm, ModelChoiceField, HiddenInput, formset_factory, RadioSelect
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
        RATING_CHOICES = [(i, str(i)) for i in range(0, 6)]
        widgets = {
            'rating': RadioSelect(choices=RATING_CHOICES),
        }
