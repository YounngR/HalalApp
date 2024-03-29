# Generated by Django 2.1.4 on 2019-10-27 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Recipe_name', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('1', '한식'), ('2', '일식'), ('3', '중식')], max_length=20)),
                ('Recipe_date', models.DateTimeField(null=True)),
                ('Recipe_image', models.ImageField(blank=True, default='photo', null=True, upload_to='')),
                ('Recipe_etc', models.CharField(max_length=20, null=True)),
                ('Recipe_recommend', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ID', models.CharField(max_length=20)),
                ('user_PW', models.CharField(max_length=20)),
                ('e_mail', models.CharField(max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('adress', models.CharField(max_length=20, null=True)),
                ('user_date', models.DateTimeField(null=True)),
                ('user_gender', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='user_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='halalapp.User'),
        ),
    ]
