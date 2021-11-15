# Generated by Django 3.2.8 on 2021-10-20 12:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_user',
            field=models.ManyToManyField(default='lv', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='amount_collected',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='amount_uncollected',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='payment_process',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='payment_status',
            field=models.CharField(choices=[('收款中', '收款中'), ('已收款', '已收款'), ('待收款', '待收款')], default='待收款', max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(choices=[('立项', '立项'), ('上线', '上线'), ('下线', '下线')], max_length=32),
        ),
        migrations.AlterField(
            model_name='project',
            name='quality_status',
            field=models.CharField(choices=[('即将过期', '即将过期'), ('已过期', '已过期'), ('质保中', '质保中')], default='质保中', max_length=255),
        ),
    ]
