from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('request_leave/', views.request_leave, name='request_leave'),
    path('success/', views.success_page, name='success_page'),
    path('leave_status/', views.leave_request_status, name='leave_request_status'),
    path('approve_leave/<int:leave_id>/', views.approve_leave, name='approve_leave'),
    path('reject_leave/<int:leave_id>/', views.reject_leave, name='reject_leave'),
    path('leave-request/', views.leave_request_view, name='request_leave'),
    path('test-template/', views.test_template, name='test_template'),

]
