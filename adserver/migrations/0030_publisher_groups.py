# Generated by Django 2.2.13 on 2020-08-17 18:28
import django_extensions.db.fields
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('adserver', '0029_publisher_payouts'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublisherGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(help_text='Visible to advertisers', max_length=200, verbose_name='Name')),
                ('slug', models.SlugField(max_length=200, verbose_name='Publisher group slug')),
                ('publishers', models.ManyToManyField(blank=True, help_text='A group of publishers that can be targeted by advertisers', related_name='publisher_groups', to='adserver.Publisher')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='campaign',
            name='publisher_groups',
            field=models.ManyToManyField(blank=True, help_text='Ads for this campaign are eligible for display on publishers in any of these groups', to='adserver.PublisherGroup'),
        ),
    ]
