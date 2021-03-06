# Generated by Django 4.0 on 2022-07-03 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='address',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='appuser',
            name='major_health_issue',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='diet',
            name='health_status',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='healthstatus',
            name='user',
            field=models.BigIntegerField(),
        ),
    ]
