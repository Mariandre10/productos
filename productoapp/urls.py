from django.urls import path
from . import views
from .views import Home, EditProduct, DeleteProduct, Logout, Login

urlpatterns = [
    path('', Login.as_view(), name='log_in'),
    path('logout/', Logout.as_view(), name='log_out'),
    path('user/logged_in/home', Home.as_view(), name='home'),
    path('user/logged_in/<int:pk>/delete_employee', DeleteProduct.as_view(), name="delete_product"),
    path('user/logged_in/<int:pk>/edit_employee', EditProduct.as_view(), name="edit_product")
]
