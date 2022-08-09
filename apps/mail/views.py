from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.template.loader import render_to_string


class SendMailView(APIView):
    def post(self, request, format=None):

        user = self.request.user
        data = self.request.data

        fullname = str(data['fullname'])

        mailContent = {
            'name': fullname,
        }

        html = render_to_string('send_mail.html', {'mail': mailContent})
        try:
            send_mail(
                subject='A cool subject',
                message='A stunning message',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                html_message=html
            )
            return Response(
                {'success': 'send email'+" "+fullname},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'failed to send email'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
