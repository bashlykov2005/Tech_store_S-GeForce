from django.urls import path

from carts import views

app_name = 'carts'

urlpatterns = [
    path("cart_add/<slug:product_slug>/", views.cart_add, name="cart_add"),
    path("cart_remove/<int:cart_id>/", views.cart_remove, name="cart_remove"),
    path("cart_update/<int:cart_id>/", views.cart_update, name="cart_update"),
    path("can_increase/<int:cart_id>/", views.can_increase, name="can_increase"),
]
