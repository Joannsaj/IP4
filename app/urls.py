from . import views
from .views import NeighbourhoodSerializer, ProfileSerializer
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"create_hood", NeighbourhoodSerializer)
router.register(r"profile", ProfileSerializer)

urlpatterns=[
    path('', views.welcome, name='welcome'),
    path('api/user/', views.UserListView.as_view()),
    # path('api/user/user-id/<int:pk>',views.UserDescription.as_view())
] + router.urls
