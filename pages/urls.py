from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('about_us/', views.AboutUsPageView.as_view(), name='about_us_page'),    
    path('profile/', views.ProfilePageView.as_view(), name='profile_page'),    
]
