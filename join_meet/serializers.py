from rest_framework import serializers


class JoinGoogleMeetSerializer(serializers.Serializer):
    meet_url = serializers.CharField(max_length=200)

    def validate(self, attrs):
        if not attrs['meet_url'].startswith("https://meet.google.com/"):
            attrs['error'] = "This is not a google meet url."
            return attrs

        return attrs

    def create(self, validated_data):
        ...

    def update(self, instance, validated_data):
        ...


class JoinZoomMeetSerializer(serializers.Serializer):
    zoom_url = serializers.CharField(max_length=200)

    def validate(self, attrs):
        if not attrs["zoom_url"].startswith("https://us05web.zoom.us/"):
            attrs['error'] = "This is not a zoom meet url."
            return attrs

        return attrs

    def create(self, validated_data):
        ...

    def update(self, instance, validated_data):
        ...


class JoinTeamsMeetSerializer(serializers.Serializer):
    teams_url = serializers.CharField(max_length=200)

    def validate(self, attrs):
        if not attrs["teams_url"].startswith("https://teams.live.com/"):
            attrs['error'] = "This is not a teams meet url."
            return attrs

        return attrs

    def create(self, validated_data):
        ...

    def update(self, instance, validated_data):
        ...
