from django.urls import path

from join_meet.views import JoinMeetAPIView


urlpatterns = [
    path('join_meet/google-meet/', JoinMeetAPIView.as_view()),
]
