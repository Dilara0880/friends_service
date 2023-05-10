from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('send_friend_request/', views.send_friend_request, name='send_friend_request'),
    path('friend_requests/handle/<int:friend_request_id>/<str:action>/', views.handle_request, name='handle_request'),

]
