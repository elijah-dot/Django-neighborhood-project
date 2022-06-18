from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),  
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout')
]
