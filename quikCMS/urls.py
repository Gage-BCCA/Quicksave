from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/', views.cms_landing, name="cms_landing"),
]