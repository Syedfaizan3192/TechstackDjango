from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise serializers.ValidationError({'message': "User with this email does not exist."})

            if not user.check_password(password):
                raise serializers.ValidationError({'message': "Incorrect password."})

            attrs['user'] = user
            return attrs
        else:
            raise serializers.ValidationError("Both email and password are required.")


class RegisterSerializer(serializers.ModelSerializer):
    cnfrm_password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "email", "cnfrm_password"]
        write_only_fields = "cnfrm_password",

    def validate(self, data):
        password = data.get('password')
        cnfrm_password = data.get('cnfrm_password')
        email = data.get('email')

        if password != cnfrm_password:
            raise serializers.ValidationError('Password not matched')
        if not email:
            raise serializers.ValidationError('Email is required')
        if not password:
            raise serializers.ValidationError('Password is required')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exists')
        return data

    def save(self):
        password = self.validated_data['password']
        email = self.validated_data['email']
        username = self.validated_data['username']

        account = User(email=email, username=username)
        account.set_password(password)
        account.save()

        return account


__all__ = [
    'RegisterSerializer'
    , 'CustomAuthTokenSerializer'
]
