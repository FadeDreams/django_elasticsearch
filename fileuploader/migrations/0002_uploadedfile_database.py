# Generated by Django 4.2.3 on 2023-08-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileuploader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='database',
            field=models.CharField(choices=[('elasticsearch', 'Elasticsearch'), ('mongodb', 'MongoDB')], default='elasticsearch', max_length=15),
        ),
    ]
