from django.urls import path
from . import views

app_name="brands_app"

urlpatterns = [
    path('', views.all_brands_view, name='all_brands_view'),
    path('<int:id>/', views.brand_detail_view, name='brand_detail_view'),  
    path('new/', views.new_brand_view, name='new_brand_view'),
    path('update/<int:id>/', views.update_brand_view, name='update_brand_view'),
]