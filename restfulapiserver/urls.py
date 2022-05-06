# from django.conf.urls import url, include
from addresses import views
from django.urls import path, re_path, include
from django.contrib import admin


urlpatterns = [
    path('addresses/', views.address_list),
    path('addresses/<int:pk>/', views.address),
    path('login/', views.login),
    path('app_login/', views.app_login),
    path('admin/', admin.site.urls),
    path('', views.address_list),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('chat_service/', views.chat_service),
    path('search_keywords/', views.search_keywords),
]