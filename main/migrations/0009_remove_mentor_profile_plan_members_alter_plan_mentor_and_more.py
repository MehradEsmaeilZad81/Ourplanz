# Generated by Django 4.1.4 on 2023-01-04 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_tag_featured_plan_remove_plan_tags_plan_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='profile',
        ),
        migrations.AddField(
            model_name='plan',
            name='members',
            field=models.ManyToManyField(related_name='members', to='main.profile'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentor', to='main.profile'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='tags',
            field=models.ManyToManyField(to='main.tag'),
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='Mentor',
        ),
    ]
