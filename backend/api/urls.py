from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'overtime', views.OvertimePostViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'signups', views.SignupViewSet)
router.register(r'auth', views.LoginViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
]