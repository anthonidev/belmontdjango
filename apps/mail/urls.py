
from django.urls import path

from apps.mail.views import SendMailView
app_name = "mail"
urlpatterns = [
    path('send', SendMailView.as_view()),
]
