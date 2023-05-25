from django.contrib import admin

from .models import (
    TgUser,
    UserMessage,
    GPTMessage,
    Tariff,
    Payment
)


class TgUserAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'username',
        'first_name', 'last_name', 'tokens_used'
    )
    search_fields = ('username', 'chat_id')
    list_filter = ('tokens_used',)
    empty_value_display = '-пусто-'


class GPTMessageInline(admin.StackedInline):
    model = GPTMessage
    can_delete = False
    verbose_name = 'Ответ GPT бота'
    verbose_name_plural = 'Ответы GPT бота'


class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'date', 'text')
    inlines = (GPTMessageInline,)
    search_fields = ('text', 'message_id', 'user')
    list_filter = ('date', 'user')
    empty_value_display = '-пусто-'


class GPTMessageAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'date', 'gpt_model',
        'total_tokens', 'user_message'
    )
    search_fields = ('text', 'user_message', 'message_id')
    list_filter = ('date', 'gpt_model', 'total_tokens')
    empty_value_display = '-пусто-'


class TariffAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'price')
    search_fields = ('name', 'description')
    empty_value_display = '-пусто-'


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date', 'amount', 'currency', 'user')
    search_fields = ('amount', 'user', 'tg_payment_id', 'bank_payment_id')
    list_filter = ('date', 'currency')
    empty_value_display = '-пусто-'


admin.site.register(TgUser, TgUserAdmin)
admin.site.register(UserMessage, UserMessageAdmin)
admin.site.register(GPTMessage, GPTMessageAdmin)
admin.site.register(Tariff, TariffAdmin)
admin.site.register(Payment, PaymentAdmin)
