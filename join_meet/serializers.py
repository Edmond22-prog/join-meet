from rest_framework import serializers


class JoinMeetSerializer(serializers.Serializer):
    meet_url = serializers.CharField(max_length=200)

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        ...

    def update(self, instance, validated_data):
        ...
