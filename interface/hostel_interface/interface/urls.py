from django.urls import path
from interface import views


app_name = 'interface'

urlpatterns = [
    path('add-booking.html/', views.add_booking),
    path('all-booking.html/', views.all_booking),
    path('all-rooms.html/', views.all_room),
    path('add-room.html/', views.add_room),
    path('all-customer.html/', views.all_customer),
    path('all-customer/<int:id>', views.del_customer),
    path('edit-customer/<int:id>', views.edit_customer),
    path('add-placetype.html', views.add_placetype),
    path('placetypes.html', views.all_placetype),
    path('placetypes/<int:id>', views.del_placetype),
    path('services.html', views.all_services),
    path('services/<int:id>', views.del_services),
    path('add-service.html', views.add_service),
    path('login.html', views.login),
    path('post-login-user-index.html', views.postLoginUser),
    path('post-login-admin-index.html', views.postLoginAdmin),
    path('user-add-booking.html/', views.user_add_booking),
    path('user-all-rooms.html/', views.user_all_room),
    path('user-placetypes.html', views.user_all_placetype),
    path('user-services.html', views.user_all_services),
    path('reviews.html/', views.get_reviews),
]