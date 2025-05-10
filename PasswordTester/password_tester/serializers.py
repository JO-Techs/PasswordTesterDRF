from rest_framework import serializers

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100, write_only=True)
    strength = serializers.CharField(read_only=True)
    feedback = serializers.CharField(read_only=True)