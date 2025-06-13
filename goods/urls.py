from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path("search/", views.catalog, name="search"),
    path("<slug:category_slug>/", views.catalog, name="index"),
    path("product/<slug:product_slug>/", views.product, name="product"),
    path("favorites/toggle/", views.toggle_favorite, name="toggle_favorite"),
]
