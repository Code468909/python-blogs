# Generated by Django 2.1.8 on 2019-05-26 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gsoc', '0017_userprofile_proposal_confirmed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adduserlog',
            options={'verbose_name': 'Add Users (The invites will be sent to the emails on save)', 'verbose_name_plural': 'Add Users (The invites will be sent to the emails on save)'},
        ),
        migrations.AddField(
            model_name='reglink',
            name='reminder',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reglinks', to='gsoc.Scheduler'),
        ),
        migrations.AlterField(
            model_name='scheduler',
            name='command',
            field=models.CharField(choices=[('send_email', 'send_email'), ('send_irc_msg', 'send_irc_msg'), ('deactivate_user', 'deactivate_user'), ('send_reg_reminder', 'send_reg_reminder')], max_length=20),
        ),
    ]
