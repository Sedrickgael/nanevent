# Generated by Django 2.2.6 on 2019-10-10 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie_event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('date_udapte', models.DateField()),
                ('dat_add', models.DateField()),
                ('statut', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'categorie_event',
                'verbose_name_plural': 'categorie_events',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('statut', models.BooleanField(default=False)),
                ('date_udapte', models.DateField()),
                ('dat_add', models.DateField()),
            ],
            options={
                'verbose_name': 'Commune',
                'verbose_name_plural': 'Communes',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Compagnie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_compagnie', models.CharField(max_length=255)),
                ('addresse', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('statut', models.BooleanField(default=False)),
                ('date_udapte', models.DateField()),
                ('dat_add', models.DateField()),
            ],
            options={
                'verbose_name': 'Compagnie',
                'verbose_name_plural': 'Compagnies',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_event', models.CharField(max_length=50)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('description', models.CharField(max_length=255)),
                ('lieu', models.CharField(max_length=255)),
                ('date_udapte', models.DateField()),
                ('dat_add', models.DateField()),
                ('statut', models.BooleanField(default=False)),
                ('compagnie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_compagnie', to='appevent.Compagnie')),
                ('id_categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_categorie', to='appevent.Categorie_event')),
                ('id_commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_commune', to='appevent.Commune')),
            ],
            options={
                'verbose_name': 'Events',
                'verbose_name_plural': 'Events',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacts', models.CharField(max_length=30, null=True)),
                ('date_udapte', models.DateField()),
                ('dat_add', models.DateField()),
                ('statut', models.BooleanField(default=False)),
                ('id_commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appevent.Commune')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Users',
                'verbose_name_plural': 'Users',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_udapte', models.DateField()),
                ('dat_add', models.DateField()),
                ('statut', models.BooleanField(default=False)),
                ('id_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant_event', to='appevent.Events')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant_user', to='appevent.Users')),
            ],
            options={
                'verbose_name': 'Participants',
                'verbose_name_plural': 'Eventss',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
