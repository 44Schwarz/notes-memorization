# Generated by Django 2.0.7 on 2018-07-29 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_review_counter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='review_counter',
            new_name='reviews_counter',
        ),
        migrations.AddField(
            model_name='note',
            name='link_file',
            field=models.FileField(default=None, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='note',
            name='link_url',
            field=models.URLField(default=''),
        ),
    ]
