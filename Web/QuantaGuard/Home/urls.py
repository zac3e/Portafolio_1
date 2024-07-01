from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='HOME'),
    path('living/', views.living, name='living')
]