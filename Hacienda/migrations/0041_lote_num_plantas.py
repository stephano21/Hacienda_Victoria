# Generated by Django 4.2.1 on 2024-02-06 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hacienda', '0040_lote_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='lote',
            name='Num_Plantas',
            field=models.IntegerField(null=True),
        ),
    ]