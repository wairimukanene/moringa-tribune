# Generated by Django 4.0.4 on 2022-05-26 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_tags_alter_editor_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editor',
            options={},
        ),
        migrations.AddField(
            model_name='editor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('post', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new.editor')),
                ('tag', models.ManyToManyField(to='new.tags')),
            ],
        ),
    ]
