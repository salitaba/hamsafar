from hamsafar.api.v1.views import ProfileView, RequestView, ProfileAPIView, RequestAPIView, FindNearAPIView, LastRequestAPIView

from django.urls import path

app_name = 'hamsafar'

urlpatterns = [
    path('profile/', ProfileAPIView.as_view()),
    path('request/', RequestAPIView.as_view()),
    path('find-near/', FindNearAPIView.as_view()),
    path('request/last/', LastRequestAPIView.as_view()),
]