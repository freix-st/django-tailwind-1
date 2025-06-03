from django.urls import path
from . import views # Import your views module

urlpatterns = [
    path('inner-page', views.inner_page, name='inner_page'), # Example: /myapp/about/
    ]