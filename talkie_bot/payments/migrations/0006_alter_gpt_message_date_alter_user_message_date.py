# Generated by Django 4.1.7 on 2023-03-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_alter_gpt_message_options_alter_payment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpt_message',
            name='date',
            field=models.FloatField(blank=True, verbose_name='Время сообщения от GPT чата'),
        ),
        migrations.AlterField(
            model_name='user_message',
            name='date',
            field=models.FloatField(blank=True, verbose_name='Время сообщения'),
        ),
    ]