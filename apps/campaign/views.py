
from rest_framework import status, generics, permissions
from apps.campaign.models import ListContact, ListItemContact
from rest_framework.response import Response

from apps.campaign.serializers import ClientSerializer, ListClientSerializer, ListItemClientSerializer
from rest_framework.pagination import PageNumberPagination


class ListClientView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = PageNumberPagination
    serializer_class = ListClientSerializer
    queryset = ListContact.objects.all()

    def list(self, request, format=None):
        # user = self.request.user
        queryset = self.get_queryset()

        # queryset = queryset.filter(user=user)
        serializer = self.serializer_class(
            queryset, many=True, context={'request': request})
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)


class ListClientDetailView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = PageNumberPagination
    serializer_class = ListItemClientSerializer
    queryset = ListItemContact.objects.all()

    def list(self, request, slug):
        queryset = self.get_queryset()
        list_client = ListContact.objects.get(slug=slug)
        queryset = queryset.filter(list_client=list_client)
        serializer = self.serializer_class(
            queryset, many=True, context={'request': request})
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)
