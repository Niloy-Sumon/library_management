# Generated by Django 4.2.7 on 2023-12-30 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='description',
        ),
        migrations.AddField(
            model_name='post',
            name='borrowing_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
    ]