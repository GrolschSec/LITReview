from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import SignUpForm


class SignupPageView(CreateView):
    form_class = SignUpForm
    template_name = "authentication/signup.html"
    success_url = reverse_lazy("flow")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(
            self.request, self.object
        )  # Log in the user after successful registration
        return response
