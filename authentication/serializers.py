from rest_framework import serializers
from .models import User, Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'roles', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        roles_data = validated_data.pop('roles')
        user = User.objects.create_user(**validated_data)
        for role_data in roles_data:
            role, _ = Role.objects.get_or_create(**role_data)
            user.roles.add(role)
        return user