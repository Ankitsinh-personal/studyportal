# Generated by Django 3.0.1 on 2020-04-24 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study_portal', '0017_auto_20200312_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='que_id',
        ),
        migrations.AddField(
            model_name='question',
            name='a',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='study_portal.Answer'),
        ),
    ]