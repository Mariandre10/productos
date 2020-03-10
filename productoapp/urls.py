from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_in, name='log_in'),
    path('', views.log_out, name='log_out'),
    path('user/logged_in/home', views.home, name='home'),
    path('user/logged_in/table', views.table, name='table'),
    path('user/logged_in/<int:pk>/delete_employee', views.delete_product, name="delete_product"),
    path('user/logged_in/<int:pk>/edit_employee', views.edit_product, name="edit_product")
]
