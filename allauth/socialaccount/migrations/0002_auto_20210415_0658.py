# Generated by Django 3.1.7 on 2021-04-15 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('socialaccount', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='socialaccount',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='socialtoken',
            unique_together={('app', 'account')},
        ),
        migrations.AlterUniqueTogether(
            name='socialaccount',
            unique_together={('provider', 'uid')},
        ),
    ]
