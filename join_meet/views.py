from rest_framework import generics
from rest_framework.response import Response

from join_meet.google_meet import join_meet
from join_meet.serializers import JoinGoogleMeetSerializer


class JoinGoogleMeetAPIView(generics.GenericAPIView):
    serializer_class = JoinGoogleMeetSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data.get('error'):
            return Response({'error': serializer.validated_data['error']})

        join_meet(serializer.validated_data['meet_url'])

        return Response({'status': 'ok'})
