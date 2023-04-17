from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.core.exceptions import ValidationError
from .forms import TicketForm, ReviewForm
from .models import Ticket, Review
from itertools import chain


class CreateTicketView(LoginRequiredMixin, CreateView):
    form_class = TicketForm
    template_name = "ticket/create_ticket.html"
    model = Ticket
    success_url = reverse_lazy("feed")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ModifyTicketView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    success_url = reverse_lazy("posts")
    template_name = "ticket/modify_ticket.html"
    fields = ["title", "description", "image"]

    def test_func(self):
        ticket = self.get_object()
        return ticket.user == self.request.user


class DeleteTicketView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ticket
    success_url = reverse_lazy("posts")
    template_name = "ticket/ticket_confirm_delete.html"

    def test_func(self):
        ticket = self.get_object()
        return ticket.user == self.request.user


class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "ticket/create_review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ticket_id = self.kwargs.get("ticket_id")

        if ticket_id:
            ticket = Ticket.objects.get(id=ticket_id)
            context["ticket"] = ticket
        else:
            context["ticket_form"] = TicketForm()
        return context

    def form_valid(self, form):
        ticket_id = self.kwargs.get("ticket_id")
        ticket = None
        if ticket_id:
            ticket = Ticket.objects.get(id=ticket_id)
        else:
            ticket_form = TicketForm(self.request.POST, self.request.FILES)
            if ticket_form.is_valid():
                ticket = ticket_form.save(commit=False)
                ticket.user = self.request.user
                ticket.save()  # Save the ticket instance
            else:
                form.add_error(None, ValidationError("Ticket form is invalid"))
                return self.form_invalid(form)
        review = form.save(commit=False)
        review.ticket = ticket
        review.user = self.request.user
        review.save()
        return redirect("feed")


class ModifyReviewView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ["headline", "rating", "body"]
    template_name = "ticket/modify_review.html"

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy("posts")


class DeleteReviewView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = "ticket/delete_review.html"
    success_url = reverse_lazy("posts")

    def test_func(self):
        review = self.get_object()
        return review.user == self.request.user


class PostView(LoginRequiredMixin, ListView):
    template_name = "ticket/posts.html"

    def get_queryset(self):
        user_tickets = Ticket.objects.filter(user=self.request.user)
        user_reviews = Review.objects.filter(user=self.request.user)
        combined = sorted(
            chain(user_tickets, user_reviews),
            key=lambda obj: obj.time_created,
            reverse=True,
        )
        return combined


class FeedView(LoginRequiredMixin, ListView):
    template_name = "ticket/feed.html"

    def get_queryset(self):
        tickets = Ticket.objects.all()
        reviews = Review.objects.all()
        combined = sorted(
            chain(tickets, reviews), key=lambda obj: obj.time_created, reverse=True
        )
        return combined
