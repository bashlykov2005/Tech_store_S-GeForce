from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('send/', views.send_feedback, name='send'),
]
