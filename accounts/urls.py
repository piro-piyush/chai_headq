from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    # Auth
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # Profile
    path("profile/", views.profile_view, name="profile"),
    path("edit-profile/", views.edit_profile_view, name="edit_profile"),

    # Password
    path("password-reset/", views.password_reset_view, name="password_reset"),
    path("password-change/", views.password_change_view, name="password_change"),
]
