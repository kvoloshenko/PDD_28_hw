from django.urls import path
from blogapp import views


app_name = 'blogapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('history/', views.history, name='history'),
    path('result/<int:id>/', views.create_result, name='result'),
    path('form/', views.create_form, name='form'),
    path('contacts/', views.create_contacts, name='contacts'),
    path('req_list/', views.Hh_RequestListView.as_view(), name='req_list'),
    path('req_detail/<int:pk>/', views.Hh_RequestDetailView.as_view(), name='req_detail'),
    path('req_create/', views.Hh_RequestCreateView.as_view(), name='req_create'),
    path('req_update/<int:pk>/', views.Hh_RequestUpdateView.as_view(), name='req_update'),
    path('req_delete/<int:pk>/', views.Hh_RequestDeleteView.as_view(), name='req_delete'),
]