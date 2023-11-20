from django.urls import path, include
from .views import *


app_name = "blog"

urlpatterns = [
    path('', index, name='index'),
    path('posts/', posts_list, name='posts_list'),
    path('posts/<int:pk>', posts_detail, name='posts_detail'),
    path('visit_session/', get_visit_session, name='get_visit_session'),
    path('accounts/', include('django.contrib.auth.urls')),
]
