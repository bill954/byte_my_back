# Generated by Django 4.0.4 on 2023-03-24 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0004_alter_card_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='color',
            field=models.CharField(choices=[('orange', 'orange'), ('green', 'green'), ('purple', 'purple'), ('blue', 'blue')], default='purple', max_length=10),
        ),
    ]
