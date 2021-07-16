from django.urls import path, include

from rest_framework import routers
from bookstore import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'admin_users', views.UserViewSet)
router.register(r'groups',views.GroupViewSet)
router.register(r'books', views.BmsBookViewSet)
router.register(r'category', views.BmsCategoryViewSet)
router.register(r'order', views.OmsOrderViewSet)
router.register(r'cart', views.OmsCartItemViewSet)
router.register(r'user', views.UmsUserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    path('api/token/',TokenObtainPairView.as_view(),name = 'token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name = 'token_refresh'),
]
