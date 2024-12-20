from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('login/forgotpassword', views.forgot_password, name='forgot_password'),
    path('logout', views.logout, name='logout'),
    path('customer', views.customer, name='customer'),
    path('customer/<str:name>', views.customer_services, name='customer_services'),
    path('customer/buy/<int:service_id>', views.buy_service, name='buy_service'),
    path('customer/buy/cart', views.cart, name='cart'),
    path('customer/buy/cart/remove/<int:item_id>', views.remove_from_cart, name='remove_from_cart'),
    path('service-provider', views.service_provider, name='service-provider'),
    path('service-provider/<str:name>', views.sp_services, name='sp_services'),
    path('portfolio-details', views.portfolio_details, name='portfolio-details'),
    path('user-form', views.user_form, name='user-form'),
    path('sp-form', views.sp_form, name='sp-form'),
    path('contact', views.contact, name='contact'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('service-provider/delete/<int:service_id>', views.delete_service, name='delete'),
    path('feedback', views.feedback, name='feedback'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)