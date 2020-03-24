
from .serializer import MyUserSerializer
from .models import MyUser
from rest_framework import viewsets
from rest_framework import status, views
# from rest_framework import generics
# from django.shortcuts import render
# from rest_framework.permissions import IsAuthenticated


# class AccountCreateAPIView(views.APIView):

#     def post(self, request, *args, **kwargs):

#         serializer = MyUserSerializer(request.data)
#         print(f'{"="*45}')
#         print(serializer.data)
#         print(f'{"="*45}')
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         print(f'{"="*45}')
#         print(serializer.data)
#         print(f'{"="*45}')


# ======================================================================

# うまくできたもの

class AccountViewSet(viewsets.ModelViewSet):

    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all()

    # def post(self, request):
    #     print(f'{"="*45}')
    #     print("ポストきた")

# ======================================================================
