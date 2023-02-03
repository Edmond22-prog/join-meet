from rest_framework import generics
from rest_framework.response import Response

from join_meet.google_meet import join_google_meet
from join_meet.serializers import JoinGoogleMeetSerializer, JoinZoomMeetSerializer, JoinTeamsMeetSerializer
from join_meet.teams_meet import join_teams_meet
from join_meet.zoom_meet import join_zoom_meet


class JoinGoogleMeetAPIView(generics.GenericAPIView):
    serializer_class = JoinGoogleMeetSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data.get('error'):
            return Response({'error': serializer.validated_data['error']})

        join_google_meet(serializer.validated_data['meet_url'])

        return Response({'status': 'ok'})


class JoinZoomMeetAPIView(generics.GenericAPIView):
    serializer_class = JoinZoomMeetSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data.get('error'):
            return Response({'error': serializer.validated_data['error']})

        try:
            join_zoom_meet(serializer.validated_data['zoom_url'])

            return Response({'status': 'ok'})

        except:
            return Response({
                'status': 'error occurred',
            })


class JoinTeamsMeetAPIView(generics.GenericAPIView):
    serializer_class = JoinTeamsMeetSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data.get('error'):
            return Response({'error': serializer.validated_data['error']})

        try:
            join_teams_meet(serializer.validated_data['teams_url'])

            return Response({'status': 'ok'})

        except:
            return Response({
                'status': 'error occurred',
            })
