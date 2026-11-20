from django.urls import path
from . import views


urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('items/', views.item_list, name='item_list'),
    path('items/report/', views.report_item, name='report_item'),
    path('items/<int:item_id>/claim/', views.claim_item, name='claim_item'),
]