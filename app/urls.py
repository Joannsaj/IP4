from . import views
from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('', views.welcome, name='welcome'),
    path('api/user/', views.UserList.as_view()),
]
