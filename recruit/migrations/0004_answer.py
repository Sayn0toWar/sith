# Generated by Django 2.2.6 on 2019-10-21 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0003_auto_20191020_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruit_name', models.CharField(max_length=100)),
                ('answers', models.TextField()),
            ],
        ),
    ]
