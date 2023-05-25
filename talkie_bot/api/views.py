from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters

from .serializers import (
    TgUserSerializer, UserMessageSerializer, GPTMessageSerializer,
    TariffSerializer, PaymentSerializer)
from payments.models import (
    TgUser, UserMessage, GPTMessage, Tariff)


class TgUserViewSet(viewsets.ModelViewSet):
    serializer_class = TgUserSerializer
    queryset = TgUser.objects.all()
    lookup_field = 'username'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'chat_id')


class UserMessageViewSet(viewsets.ModelViewSet):
    serializer_class = UserMessageSerializer

    def get_queryset(self):
        tg_user = get_object_or_404(
            TgUser, username=self.kwargs.get('username'))
        user_messages = tg_user.sent_msgs.all()
        return user_messages

    def perform_create(self, serializer):
        tg_user = get_object_or_404(
            TgUser, username=self.kwargs.get('username'))
        serializer.save(user=tg_user)


class GPTMessageViewSet(viewsets.ModelViewSet):
    serializer_class = GPTMessageSerializer
    queryset = GPTMessage.objects.all()

    def perform_create(self, serializer):
        user_message = get_object_or_404(
            UserMessage,
            message_id=self.request.data['user_message'])
        serializer.save(user_message=user_message)


class TariffViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TariffSerializer
    queryset = Tariff.objects.all()
    lookup_field = 'price'


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        tg_user = get_object_or_404(
            TgUser, username=self.kwargs.get('username'))
        payments = tg_user.payments.all()
        return payments

    def perform_create(self, serializer):
        tg_user = get_object_or_404(
            TgUser, username=self.kwargs.get('username'))
        serializer.save(user=tg_user)
