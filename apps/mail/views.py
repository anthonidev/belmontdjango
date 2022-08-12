from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.template.loader import render_to_string



class SendMailView(APIView):
    def post(self, request, slug, format=None):

        # user = self.request.user
        # # data = self.request.data
        # campaing = Campaign.objects.get(slug=slug)

        # people = []

        # for list_campaign in campaing.list_client.all():
        #     items_client = ListItemClient.objects.filter(
        #         list_client__slug=list_campaign.slug)
        #     for list_client in items_client:
        #         if list_client.client.id not in people:
        #             people.append(list_client.client.id)

        # count = 0
        # for person in people:
        #     client = Client.objects.get(id=person)
        #     mailContent = {
        #         'name': client.name,
        #         'lastname': client.lastname,
        #     }

        #     html = render_to_string('send_mail.html', {'mail': mailContent})
        #     try:
        #         send_mail(
        #             subject='A cool subject',
        #             message='A stunning message',
        #             from_email=settings.EMAIL_HOST_USER,
        #             recipient_list=[client.email],
        #             html_message=html
        #         )
        #         count += 1
        #         print("send: ", client.email)

        #     except:
        #         pass

        return Response({"Correos enviados": 2})
