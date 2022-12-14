# Generated by Django 4.1.4 on 2022-12-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_profilemodel_batch"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profilemodel",
            name="batch",
        ),
        migrations.AddField(
            model_name="profilemodel",
            name="batch_fee",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="profilemodel",
            name="batch_slots",
            field=models.IntegerField(
                choices=[(1, "6-7AM"), (2, "7-8AM"), (3, "8-9AM"), (4, "5-6PM")],
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="profilemodel",
            name="batchmonth",
            field=models.CharField(
                choices=[
                    ("DEC", "December"),
                    ("JAN", "January"),
                    ("FEB", "February"),
                    ("MAR", "March"),
                    ("APR", "April"),
                    ("MAY", "May"),
                    ("JUN", "June"),
                    ("JUL", "July"),
                    ("AUG", "August"),
                    ("SEP", "September"),
                    ("OCT", "October"),
                    ("NOV", "November"),
                ],
                max_length=3,
                null=True,
            ),
        ),
    ]
