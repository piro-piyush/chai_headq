from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    # path("", views.feed, name="feed"),
    path("register/", views.register, name="register"),    # User signup
    path("login/", views.login_view, name="login"),        # User login
    path("logout/", views.logout_view, name="logout"),     # User logout
    path("password-reset/", views.password_reset, name="password_reset"),  # Reset password
    path("password-change/", views.password_change, name="password_change"),  # Change password
   path("profile/<str:username>/", views.profile, name="profile")
]  