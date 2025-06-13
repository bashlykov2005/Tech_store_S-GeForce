from django.urls import path

from users import views
from users.views import (CustomPasswordChangeView,)

app_name = 'users'

urlpatterns = [
    path("login/", views.login, name="login"),
    path("registration/", views.registration, name="registration"),
    path("profile/", views.profile, name="profile"),
    path("users-cart/", views.users_cart, name="users_cart"),
    path("logout/", views.logout, name="logout"),
    path(
        "password-change/", CustomPasswordChangeView.as_view(), name="password_change"
    ),
    path("delete-account/", views.delete_account, name="delete_account"),
    path("favorites/", views.favorites, name="favorites"),
    path("orders/", views.user_orders, name="orders"),
]
