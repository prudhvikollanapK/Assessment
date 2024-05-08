from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.account_list),
    path('accounts/<int:pk>/', views.account_detail),
    path('accounts/<int:account_id>/destinations/', views.create_destination),
    path('accounts/<int:account_id>/destinations/', views.list_destinations),
    path('receive_data/', views.receive_data),
]