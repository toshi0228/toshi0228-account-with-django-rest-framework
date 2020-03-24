from django.urls import path, include
from plan import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('', views.PlanViewSet)

urlpatterns = [
    path('', include(router.urls))
]


# 参考
# ==================================================================================================
# from django.urls import path, include
# from account import views
# from rest_framework import routers
# # ======================================================================

# # うまくできたもの
# router = routers.DefaultRouter()
# router.register('register', views.AccountViewSet)

# urlpatterns = [
#     path('', include(router.urls))
# ]

# # ======================================================================

# ==================================================================================================
