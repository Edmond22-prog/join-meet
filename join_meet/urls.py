from django.urls import path

from join_meet.views import JoinGoogleMeetAPIView


urlpatterns = [
    path('join_meet/google-meet/', JoinGoogleMeetAPIView.as_view()),
]
