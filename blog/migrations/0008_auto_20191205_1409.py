# Generated by Django 2.2.5 on 2019-12-05 06:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190925_1701'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='confirmstring',
            options={'ordering': ['-created'], 'verbose_name': '确认码', 'verbose_name_plural': '确认码'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-created'], 'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='create_time',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='update_time',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='confirmstring',
            old_name='create_time',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='user',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='user',
            name='has_confirmed',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sex',
        ),
        migrations.AddField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(0, '保密'), (1, '男'), (2, '女')], default=0, verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=256, verbose_name='手机号'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(0, '普通会员'), (1, '管理员')], default=0, verbose_name='角色'),
        ),
        migrations.AddField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='更新时间'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(default='', max_length=256, verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=256, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=128, unique=True, verbose_name='用户名'),
        ),
    ]
