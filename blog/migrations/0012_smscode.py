# Generated by Django 2.2.5 on 2019-12-06 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20191205_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmsCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '验证码',
                'verbose_name_plural': '验证码',
                'ordering': ['-created'],
            },
        ),
    ]