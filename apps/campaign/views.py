
from rest_framework import status, generics, permissions
from apps.campaign.models import ListClient
from rest_framework.response import Response

from apps.campaign.serializers import ListClientSerializer


class ListClientView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = None
    serializer_class = ListClientSerializer
    queryset = ListClient.objects.all()

    def list(self, request, format=None):
        user = self.request.user
        queryset = self.get_queryset()
        return Response(
            {'lists': self.serializer_class(queryset).data},
            status=status.HTTP_200_OK
        )
