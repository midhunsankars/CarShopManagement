# Generated by Django 3.1.2 on 2020-10-28 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logintable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'Logintable',
            },
        ),
    ]