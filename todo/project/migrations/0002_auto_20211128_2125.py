# Generated by Django 3.2.9 on 2021-11-28 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todo',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
    ]
