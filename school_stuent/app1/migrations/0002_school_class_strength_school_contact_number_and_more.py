# Generated by Django 4.2.3 on 2023-07-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='class_strength',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='contact_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='teacher_strength',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
