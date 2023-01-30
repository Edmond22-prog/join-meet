from rest_framework import generics
from rest_framework.response import Response

from join_meet.google_meet import join_meet
from join_meet.serializers import JoinMeetSerializer


class JoinMeetAPIView(generics.GenericAPIView):
    serializer_class = JoinMeetSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        join_meet(serializer.validated_data['meet_url'])

        return Response({'status': 'ok'})
