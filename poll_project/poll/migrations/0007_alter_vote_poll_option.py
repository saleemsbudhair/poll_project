# Generated by Django 3.2.8 on 2021-10-15 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0006_remove_poll_most_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='poll_option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='poll.polloption'),
        ),
    ]