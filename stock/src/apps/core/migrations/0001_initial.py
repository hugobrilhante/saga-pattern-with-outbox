# Generated by Django 4.2.8 on 2024-01-18 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=20)),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
