from django.urls import path
from . import views

app_name = 'assets'

urlpatterns = [
    path('rezervacija/', views.your_form_view, name='rezervacija'),
    ]