from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),  
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'), 
    path('hoods/', views.n_hoods, name='n_hoods'), 
    path('join/(\d+)', views.join, name='join-hood'), 
    path('leave/(\d+)', views.leave, name='leave-hood'),
    path('hood/(\d+)', views.my_hood, name='my-hood'),
    path('business/(\d+)', views.business, name='hood-business'),
    path('contacts/(\d+)', views.contacts, name='hood-contacts'),
    path('announcements/(\d+)', views.announcements, name='announcements'),
    path('search/', views.search_results, name='search'),
    
]
