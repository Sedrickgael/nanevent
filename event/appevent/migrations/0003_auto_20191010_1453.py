# Generated by Django 2.2.6 on 2019-10-10 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appevent', '0002_auto_20191010_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateurs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacts', models.CharField(max_length=30, null=True)),
                ('date_udapte', models.DateField()),
                ('dat_add', models.DateField()),
                ('statut', models.BooleanField(default=False)),
                ('id_commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_commune', to='appevent.Commune')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Users',
                'verbose_name_plural': 'Users',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='participants',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant_user', to='appevent.Utilisateurs'),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]