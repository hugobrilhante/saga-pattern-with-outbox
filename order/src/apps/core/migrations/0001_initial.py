# Generated by Django 4.2.8 on 2024-01-19 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.CharField(max_length=20)),
                ('product_id', models.CharField(max_length=20)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('amount', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('created', 'Created'), ('reserved', 'Reserved'), ('not_reserved', 'Not Reserved'), ('payment_confirmed', 'Payment Confirmed'), ('payment_denied', 'Payment Denied')], default='created', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
