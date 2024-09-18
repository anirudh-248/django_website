from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post'),
    path('services', views.services, name='services'),
    path('services/<str:name>', views.service_details, name='service_details'),
    path('portfolio-details', views.portfolio_details, name='portfolio-details'),
    path('user-form', views.user_form, name='user-form'),
    path('sp-form', views.sp_form, name='sp-form'),
    path('contact', views.contact, name='contact'),
    path('aboutus', views.aboutus, name='aboutus')
]