# Generated by Django 4.0.3 on 2022-03-11 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FollowerCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=110)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRequired',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_of_users', models.CharField(max_length=1500)),
            ],
        ),
    ]
