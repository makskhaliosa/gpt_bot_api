from django.db import models


class TgUser(models.Model):
    chat_id = models.BigIntegerField(
        'Id чата в ТГ',
        unique=True)
    username = models.CharField(
        'Username в ТГ',
        max_length=250,
        unique=True)
    first_name = models.CharField(
        'Имя в ТГ',
        max_length=250,
        blank=True)
    last_name = models.CharField(
        'Фамилия в ТГ',
        max_length=250,
        blank=True)
    tokens_used = models.IntegerField(
        'Общее количество токенов',
        null=True)
    is_staff = models.BooleanField(
        'Член команды',
        default=False
    )

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь ТГ'
        verbose_name_plural = 'Пользователи ТГ'

    def __str__(self):
        return self.username


class UserMessage(models.Model):
    message_id = models.BigIntegerField('Id сообщения пользователя')
    user = models.ForeignKey(
        TgUser,
        on_delete=models.CASCADE,
        related_name='sent_msgs',
        verbose_name='автор сообщения',
        default=0
    )
    date = models.DateTimeField('Время сообщения')
    text = models.TextField('Текст сообщения', blank=True)

    class Meta:
        ordering = ['date']
        verbose_name = 'Запрос пользователей'
        verbose_name_plural = 'Запросы пользователей'

    def __str__(self):
        return f'{self.date} - {self.text[:10]}'


class GPTMessage(models.Model):
    message_id = models.CharField(
        'Id сообщения от GPT чата',
        unique=True,
        max_length=250
    )
    date = models.DateTimeField('Время сообщения от GPT чата')
    gpt_model = models.CharField(
        'Модель GPT чата',
        max_length=250)
    total_tokens = models.IntegerField('Общее количество токенов')
    text = models.TextField(
        'Текст сообщения от GPT чата',
        blank=True)
    user_message = models.OneToOneField(
        UserMessage,
        on_delete=models.CASCADE,
        related_name='gpt_response',
        verbose_name='Запрос от пользователя',
        default=0
    )

    class Meta:
        ordering = ['date']
        verbose_name = 'Ответ GPT бота'
        verbose_name_plural = 'Ответы GPT бота'

    def __str__(self):
        return f'{self.total_tokens} - {self.text[:10]}'


class Tariff(models.Model):
    name = models.CharField(
        'Название тарифа',
        max_length=250)
    description = models.TextField('Описание тарифа')
    price = models.FloatField('Цена')

    class Meta:
        ordering = ['name']
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return f'{self.name} - {self.price}'


class Payment(models.Model):
    tg_payment_id = models.CharField('Id оплаты в ТГ', max_length=255)
    bank_payment_id = models.CharField('Id оплаты в банке', max_length=255)
    date = models.DateTimeField('Дата оплаты', auto_now_add=True)
    amount = models.FloatField('Сумма оплаты', null=True)
    currency = models.CharField(
        'Валюта оплаты',
        max_length=10,
        blank=True
    )
    user = models.ForeignKey(
        TgUser,
        on_delete=models.CASCADE,
        related_name='payments',
        default=0
    )
    tariff = models.ForeignKey(
        Tariff,
        on_delete=models.CASCADE,
        related_name='payments',
        default=0
    )

    class Meta:
        ordering = ['date']
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

    def __str__(self):
        return f'{self.date} - {self.amount}'
