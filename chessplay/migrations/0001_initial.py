# Generated by Django 4.2.5 on 2023-09-28 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moves', models.TextField()),
                ('result', models.CharField(choices=[('1:0', '1:0'), ('0:1', '0:1'), ('1/2-1/2', '1/2-1/2'), ('-:-', '-:-'), ('+:-', '+:-'), ('-:+', '-:+')], default='-:-', max_length=50)),
                ('status', models.CharField(choices=[('not started', 'Not Started'), ('ongoing', 'Ongoing'), ('finished', 'Finished')], default='not started', max_length=50)),
                ('date_played', models.DateTimeField(auto_now_add=True)),
                ('winner', models.IntegerField()),
                ('black_player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='black_player', to='registration.player')),
                ('white_player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='white_player', to='registration.player')),
            ],
        ),
    ]