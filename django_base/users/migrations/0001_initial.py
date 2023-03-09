# Generated by Django 4.0.4 on 2023-03-08 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_settings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='cover_images')),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('availability', models.CharField(blank=True, choices=[('full-time', 'full-time'), ('part-time', 'part-time'), ('freelance', 'freelance'), ('other', 'other')], max_length=30, null=True)),
                ('years_of_experience', models.PositiveIntegerField(blank=True, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='admin_settings.country')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='admin_settings.language')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
