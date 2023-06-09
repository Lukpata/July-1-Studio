# Generated by Django 4.1.3 on 2023-02-21 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs_available',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacancy', models.CharField(max_length=200, verbose_name='event_category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Vacancies',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=100)),
                ('document', models.FileField(upload_to='')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.jobs_available')),
            ],
        ),
    ]
