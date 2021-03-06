
from django.contrib import admin
from django.urls import path,include

from TarFoodApp import views,apis
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('restaurant/sign-in/', auth_views.LoginView.as_view(template_name = 'restaurant/sign-in.html'),
         name = 'restaurant-sign-in'),
    path('restaurant/sign-out/', auth_views.LogoutView.as_view(next_page = '/'),name = 'restaurant-sign-out'),
    path('restaurant/sign-up/', views.restaurant_sign_up, name='restaurant-sign-up'),
    path('restaurant/',views.restaurant_home,name = 'restaurant-home'),

    path('restaurant/account/', views.restaurant_account, name = 'restaurant-account'),
    path('restaurant/meal/', views.restaurant_meal, name = 'restaurant-meal'),
    path('restaurant/meal/add/', views.restaurant_add_meal, name = 'restaurant-add-meal'),
    path('restaurant/meal/edit/<meal_id>', views.restaurant_edit_meal, name = 'restaurant-edit-meal'),
    path('restaurant/order/', views.restaurant_order, name = 'restaurant-order'),
    path('restaurant/report/', views.restaurant_report, name = 'restaurant-report'),



    path('api/social/', include('rest_framework_social_oauth2.urls')),



    path('api/restaurant/order/notification/<last_request_time>/', apis.restaurant_order_notification),



    path('api/customer/restaurants/', apis.customer_get_restaurants),
    path('api/customer/meals/<restaurant_id>/', apis.customer_get_meals),
    path('api/customer/order/add/', apis.customer_add_order),
    path('api/customer/order/latest', apis.customer_get_latest_order),






]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
