from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    
    path('check',views.check),

    path('location/all',views.locations_get),
    path('location/post',views.location_post),
    path('location/get/<int:pk>',views.location_get),
    path('location/put/<int:pk>',views.location_put),
    path('location/delete/<int:pk>',views.location_delete),

    path('ads/all',views.ads_get),
    path('ads/post',views.ad_post),
    path('ads/get/<int:pk>',views.ad_get),
    path('ads/put/<int:pk>',views.ad_put),
    path('ads/delete/<int:pk>',views.ad_delete),

    path('ads/visits/<int:pk>',views.ad_visits)

]
