"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
import authentication.views
from authentication.views import SignupPageView
import ticket.views

urlpatterns = [
    # admin urls
    path("admin/", admin.site.urls),
    # authentication urls
    path(
        "",
        LoginView.as_view(
            template_name="authentication/login.html",
            redirect_authenticated_user=True,
            next_page="feed",
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("signup/", SignupPageView.as_view(), name="signup"),
    # blog urls
    path("feed/", ticket.views.FeedView.as_view(), name="feed"),
    path("posts/", ticket.views.PostView.as_view(), name="posts"),
    path("subscription/", authentication.views.SubscriptionView.as_view(), name="subscription"),
    # ticket urls
    path("create_ticket/", ticket.views.CreateTicketView.as_view(), name="create-ticket"),
    path('modify_ticket/<int:pk>/', ticket.views.ModifyTicketView.as_view(), name='modify-ticket'),
    path('delete_ticket/<int:pk>/', ticket.views.DeleteTicketView.as_view(), name='delete-ticket'),
    # review urls
    path('create_review/', ticket.views.CreateReviewView.as_view(), name='create-review'),
    path('create_review/<int:ticket_id>/', ticket.views.CreateReviewView.as_view(), name='create-review'),
    path('modify_review/<int:review_id>/', ticket.views.ModifyTicketView.as_view(), name='modify-review'),
    # path('delete_review/<int:review_id>/', ticket.views.DeleteReviewView.as_view(), name='delete-review')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
