from django.views.generic.edit import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import SignUpForm
from .models import CustomUser


class SignupPageView(CreateView):
    form_class = SignUpForm
    template_name = "authentication/signup.html"
    success_url = reverse_lazy("feed")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class SubscriptionView(LoginRequiredMixin, View):
    template_name = "authentication/user_follow.html"

    def get(self, request, *args, **kwargs):
        following = request.user.following.all()
        followers = CustomUser.objects.filter(following__in=[request.user])
        return render(
            request,
            self.template_name,
            {"following": following, "followers": followers},
        )

    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")

        if action == "subscribe":
            username = request.POST.get("username")
            if username == request.user.username:
                return redirect("subscription")
            user_to_follow = CustomUser.objects.filter(username=username).first()
            if user_to_follow:
                request.user.following.add(user_to_follow)
                messages.success(request, "Successfully subscribed to the user.")
            else:
                messages.error(
                    request, "Failed to subscribe to the user. User not found."
                )
            return redirect("subscription")

        elif action == "unsubscribe":
            username = request.POST.get("username")
            user_to_unfollow = CustomUser.objects.filter(username=username).first()
            request.user.following.remove(user_to_unfollow)
            messages.success(request, "Successfully unsubscribed from the user.")
            return redirect("subscription")

        else:
            messages.error(request, "Invalid action.")
            return redirect("subscription")
