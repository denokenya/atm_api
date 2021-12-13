from django.db import router


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from atm.views.machine_view import Machine_ViewSet



router = DefaultRouter()

router.register("machine",Machine_ViewSet, "machine")



urlpatterns = [
    path('api/token', obtain_auth_token, name='api-token'),
    path('', include(router.urls)),
]
