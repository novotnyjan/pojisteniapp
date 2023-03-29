# Generated by Django 4.1 on 2023-03-29 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pojisteniapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pojisteni",
            name="castka",
            field=models.BigIntegerField(verbose_name="Částka"),
        ),
        migrations.AlterField(
            model_name="pojisteni",
            name="predmet_pojisteni",
            field=models.CharField(
                blank=True,
                help_text="Vyplňte pouze v případě, že předmět pojištění není patrný (např. u pojištění majetku).",
                max_length=30,
                null=True,
                verbose_name="Předmět pojištění",
            ),
        ),
    ]