from django.urls import path, include
from account import views
from rest_framework import routers


# from .views import MyUserViewSet
# urlpatterns = [
#     path("register/", views.AccountCreateAPIView.as_view())
# ]


# ======================================================================

# うまくできたもの
router = routers.DefaultRouter()
router.register('register', views.AccountViewSet)

urlpatterns = [
    path('', include(router.urls))
]

# ======================================================================
