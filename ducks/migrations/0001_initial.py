# Generated by Django 2.2.5 on 2019-09-12 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Duck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duck_name', models.CharField(help_text='Enter field documentation', max_length=255)),
                ('duck_last_name', models.CharField(help_text='Enter field documentation', max_length=255)),
                ('duck_mail', models.EmailField(max_length=255)),
                ('duck_age', models.IntegerField()),
            ],
        ),
    ]
