# Generated by Django 3.2.8 on 2021-10-15 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_poll_most_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_four',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_four_count',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_one',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_one_count',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_three',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_three_count',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_two',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_two_count',
        ),
        migrations.AddField(
            model_name='poll',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='poll.poll')),
                ('poll_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.polloption')),
            ],
        ),
        migrations.AddField(
            model_name='polloption',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='poll.poll'),
        ),
    ]
