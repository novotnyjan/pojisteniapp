# Generated by Django 4.1 on 2023-03-29 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pojisteniapp", "0003_alter_pojisteni_castka"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pojistenec",
            name="jmeno",
            field=models.CharField(max_length=30, verbose_name="Jméno"),
        ),
        migrations.AlterField(
            model_name="pojistenec",
            name="prijmeni",
            field=models.CharField(max_length=30, verbose_name="Příjmení"),
        ),
    ]