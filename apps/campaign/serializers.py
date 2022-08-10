from rest_framework import serializers

from apps.campaign.models import ListClient, Client


class ListClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListClient
        fields = [
            'id',
            'title',
            'description',
            'status',
            'created_at',
            'updated_at',
            'slug',
        ]


class ClientSerializer(serializers.ModelSerializer):
    fullname = serializers.CharField(source="get_fullname")

    class Meta:
        model = Client
        fields = [
            'id',
            'name',
            'lastname',
            'email',
            'phone',
            'created_at',
            'updated_at',
            'slug',
            'fullname'
        ]


class ListItemClientSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = ListClient
        fields = [
            'id',
            'client',
            'created_at',
            'updated_at'
        ]
