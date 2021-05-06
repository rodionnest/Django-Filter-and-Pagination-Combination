from django.urls import path
from mainapp.views import StuffView


urlpatterns = [
    path('', StuffView.as_view()),
]
