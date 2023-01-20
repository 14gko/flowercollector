from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('flowers/', views.flowers_index, name='index'),
    path('flowers/<int:flower_id>/', views.flowers_detail, name='detail'),
    path('flowers/create/', views.FlowerCreate.as_view(), name='flowers_create'),
    # if flower instance exists then add int:pk
    path('flowers/<int:pk>/update/', views.FlowerUpdate.as_view(), name='flowers_update'),
    path('flowers/<int:pk>/delete/', views.FlowerDelete.as_view(), name='flowers_delete'), 
    path('flowers/<int:flower_id>/add_watering/', views.add_watering, name='add_watering'),
    path('fertilizers/', views.FertList.as_view(), name='fert_index'),
    path('fertilizers/<int:pk>/', views.FertDetail.as_view(), name='fert_detail'),
    path('fertilizers/create/', views.FertCreate.as_view(), name='fert_create'),
    path('fertilizers/<int:pk>/update/', views.FertUpdate.as_view(), name='fert_update'),
    path('fertilizers/<int:pk>/delete/', views.FertDelete.as_view(), name='fert_delete'),
    path('flowers/<int:flower_id>/assoc_fert/<int:fertilizer_id>/', views.assoc_fert, name='assoc_fert'),
    ]