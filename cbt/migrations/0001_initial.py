# Generated by Django 4.0.2 on 2022-02-25 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeelVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feel', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_datetime', models.DateTimeField()),
                ('moody', models.CharField(max_length=400, null=True)),
                ('event', models.CharField(max_length=100, null=True)),
                ('old_think', models.CharField(max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewThinking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_think', models.CharField(max_length=400)),
                ('thought', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbt.thought')),
            ],
        ),
        migrations.CreateModel(
            name='Feeling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feel_variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbt.feelvariation')),
                ('thought', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbt.thought')),
            ],
        ),
    ]
