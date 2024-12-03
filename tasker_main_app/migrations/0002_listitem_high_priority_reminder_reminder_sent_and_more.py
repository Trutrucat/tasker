# Generated by Django 4.2.16 on 2024-12-02 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker_main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listitem',
            name='high_priority',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reminder',
            name='reminder_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='list_user',
            name='role',
            field=models.CharField(choices=[('R', 'Read Only'), ('E', 'Editor')], default='R', max_length=1),
        ),
    ]
