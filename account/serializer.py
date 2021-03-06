from rest_framework import serializers
from .models import MyUser


class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fielfs = ('email', 'password', )
        exclude = ('first_name', 'last_name', "username",
                   'profile', "is_active", "is_staff", "last_login")

    def create(self, validated_data):
        print(f'{"="*105}')
        print(validated_data)
        print(f'{"="*105}')

        user = MyUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user
