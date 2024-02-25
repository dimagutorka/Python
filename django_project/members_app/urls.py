from django.urls import path, re_path
from .views import *


urlpatterns = [
path('user_input/', session_data, name='user_input'),
path('display_page/', display_view, name='display_page'),
path('is_authorized_page',is_authorized_user, name='is_authorized_page')

]