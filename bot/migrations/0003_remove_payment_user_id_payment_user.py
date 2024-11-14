# Generated by Django 4.2 on 2024-11-14 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_remove_order_status_en_remove_order_status_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='user_id',
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='bot.customuser'),
            preserve_default=False,
        ),
    ]