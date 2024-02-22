from django.urls import path
from jinja import views

urlpatterns = [
    path('', views.home, name='my_index'),
    path('about/', views.about, name='my_about'),
    path('contactus/', views.contactus, name='my_contactus'),
    path('gallery/', views.gallery, name='my_gallery')
]
