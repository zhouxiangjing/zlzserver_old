# Generated by Django 2.2.5 on 2019-12-06 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_smscode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='smscode',
            options={'ordering': ['-updated'], 'verbose_name': '验证码', 'verbose_name_plural': '验证码'},
        ),
        migrations.RenameField(
            model_name='smscode',
            old_name='created',
            new_name='updated',
        ),
    ]
