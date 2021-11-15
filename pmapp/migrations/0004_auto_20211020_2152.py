# Generated by Django 3.2.8 on 2021-10-20 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pmapp', '0003_auto_20211020_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualityrecord',
            name='quality_money',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='qualityrecord',
            name='quality_people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]