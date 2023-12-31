# Generated by Django 4.1.5 on 2023-07-26 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pp", models.ImageField(upload_to="Profile_Photo")),
                ("ac", models.ImageField(upload_to="Aadhar_Card")),
                ("pc", models.ImageField(upload_to="Pan_Card")),
                ("vip", models.ImageField(upload_to="Voter_Id_Proof")),
                ("ms", models.ImageField(upload_to="Marksheet")),
            ],
        ),
        migrations.CreateModel(
            name="Registration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=50)),
                ("Phone", models.CharField(max_length=50, unique=True)),
                ("Email", models.EmailField(max_length=254, unique=True)),
                ("Password", models.CharField(max_length=50)),
                ("Company", models.CharField(max_length=50)),
            ],
        ),
    ]
