from rest_framework import serializers

from payments.models import (
    TgUser, UserMessage, GPTMessage, Tariff, Payment)


class TgUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TgUser


class GPTMessageSerializer(serializers.ModelSerializer):
    user_message = serializers.SlugRelatedField(
        queryset=UserMessage.objects.all(),
        slug_field='message_id')

    class Meta:
        fields = '__all__'
        model = GPTMessage


class UserMessageSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    gpt_response = GPTMessageSerializer(required=False)

    class Meta:
        fields = ('id', 'user', 'message_id', 'date', 'text', 'gpt_response')
        model = UserMessage


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Tariff


class PaymentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    tariff = serializers.SlugRelatedField(
        required=True,
        slug_field='name',
        queryset=Tariff.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Payment
