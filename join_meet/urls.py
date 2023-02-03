from django.urls import path

from join_meet.views import JoinGoogleMeetAPIView, JoinZoomMeetAPIView, JoinTeamsMeetAPIView

urlpatterns = [
    path('join_meet/google-meet/', JoinGoogleMeetAPIView.as_view()),
    path('join_meet/zoom-meet/', JoinZoomMeetAPIView.as_view()),
    path('join_meet/teams-meet/', JoinTeamsMeetAPIView.as_view()),
]
