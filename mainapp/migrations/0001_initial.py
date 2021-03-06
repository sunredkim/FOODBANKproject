# Generated by Django 3.1.5 on 2021-02-10 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accountapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('writedate', models.DateTimeField(auto_now_add=True)),
                ('cnt', models.IntegerField(default=0)),
                ('like', models.IntegerField(default=0)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='recommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.board')),
                ('useremail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountapp.users')),
            ],
        ),
    ]
