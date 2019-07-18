from hamsafar.api.v1.views import ProfileView, RequestView, ProfileAPIView, RequestAPIView

from django.urls import path

app_name = 'hamsafar'

urlpatterns = [
    path('profile/', ProfileAPIView.as_view()),
    path('request/', RequestAPIView.as_view()),
]