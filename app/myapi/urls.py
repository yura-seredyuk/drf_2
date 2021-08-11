from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users-list', views.UsersViewSet)
router.register(r'address-list', views.AddressViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('address/', views.AddressViev.AddressList.as_view()),
    path('address/<int:pk>/', views.AddressViev.AddressDetail.as_view()),
]