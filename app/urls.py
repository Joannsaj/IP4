from . import views
from .views import NeighbourhoodSerializer, ProfileSerializer, PostSerializer, BusinessSerializer
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"create_hood", NeighbourhoodSerializer)
router.register(r"profile", ProfileSerializer)
router.register(r"post", PostSerializer)
router.register(r"business", BusinessSerializer)

urlpatterns=[
    path('', views.welcome, name='welcome'),
    path('api/user/', views.UserListView.as_view()),
] + router.urls
