from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('search/', views.search_products, name='search_products'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='products/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='products/logout.html'), name='logout'),
]
