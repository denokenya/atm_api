from django.db import router


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from atm.views.machine_view import Machine_ViewSet
from atm.views.machine_refill_view import Machine_Refill_ViewSet
from atm.views.account_view import Account_ViewSet



router = DefaultRouter()

router.register("machine",Machine_ViewSet, "machine")
router.register("machine_refill",Machine_Refill_ViewSet, "machine_refill")
router.register("account",Account_ViewSet, "account")



urlpatterns = [
    path('api/token', obtain_auth_token, name='api-token'),
    path('', include(router.urls)),
]
