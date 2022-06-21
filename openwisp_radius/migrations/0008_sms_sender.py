# Generated by Django 3.0.7 on 2020-06-24 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openwisp_radius', '0007_sms_verification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organizationradiussettings',
            old_name='sms_phone_number',
            new_name='sms_sender',
        ),
        migrations.AlterField(
            model_name='organizationradiussettings',
            name='sms_sender',
            field=models.CharField(
                blank=True,
                help_text=(
                    'alpha numeric identifier used as sender for '
                    'SMS sent by this organization'
                ),
                max_length=128,
                null=True,
                verbose_name='Sender',
            ),
        ),
    ]