# Generated by Django 4.1.4 on 2022-12-22 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_member_membership_plan_starts_at_remove_member_plan_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={},
        ),
        migrations.RemoveField(
            model_name='member',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='member',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='member',
            name='join_date',
        ),
        migrations.RemoveField(
            model_name='member',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='member',
            name='membership',
        ),
        migrations.RemoveField(
            model_name='member',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
        migrations.RemoveField(
            model_name='member',
            name='plan',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateTimeField(auto_created=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=14)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.plan')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.plan'),
            preserve_default=False,
        ),
    ]