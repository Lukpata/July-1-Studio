# Generated by Django 4.1.3 on 2023-02-15 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0004_rename_email_footer_news_letter_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='full_name',
            new_name='first_name',
        ),
    ]
