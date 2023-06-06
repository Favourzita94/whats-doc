from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import DefaultRouter
from knox import views as knox_views

from . import views
from .views import UsersAPI, LoginAPI, SingleUserAPI

# router = DefaultRouter()
# router.register("", UserViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('users/', UsersAPI.as_view(), name='users'),
    path('users/profile/', SingleUserAPI.as_view(), name='user'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('users/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('users/', views.all_users),
    # path('users/<str:id>/', views.all_users),
    # path('users/uploads/', views.all_users),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += router.urls