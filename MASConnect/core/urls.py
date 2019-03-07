from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as token_views
from .views import UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = []
urlpatterns += [
    path('token-auth/', token_views.obtain_auth_token)
]
urlpatterns += router.urls

