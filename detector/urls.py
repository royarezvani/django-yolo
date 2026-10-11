from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload'),
    path('result/<int:img_id>/', views.result, name='result'),
]