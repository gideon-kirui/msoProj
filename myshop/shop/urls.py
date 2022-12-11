from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('mogibe_help/', views.mogibe_help, name='mogibe_help'),
    path('mogibe_about/', views.mogibe_about, name='mogibe_about'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
] 