from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("account/register/", views.RegisterView.as_view(), name="register"),
    path('account/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('account/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
