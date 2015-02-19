# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Companion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Companionship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=256)),
                ('notes', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('moved', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('birthday', models.DateField(blank=True)),
                ('phone', models.CharField(max_length=28, blank=True)),
                ('email', models.CharField(max_length=128)),
                ('is_home_teacher', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('household', models.ForeignKey(related_name='members', to='llts.Household')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(related_name='organizations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('notes', models.TextField(blank=True)),
                ('household', models.ForeignKey(related_name='visits', to='llts.Household')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='household',
            name='organization',
            field=models.ForeignKey(related_name='households', to='llts.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='district',
            name='leader',
            field=models.ForeignKey(related_name='districts', to='llts.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='district',
            name='organization',
            field=models.ForeignKey(related_name='districts', to='llts.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='companionship',
            name='district',
            field=models.ForeignKey(related_name='companionships', to='llts.District'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='companion',
            name='companionship',
            field=models.ForeignKey(related_name='members', to='llts.Companionship'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='companion',
            name='member',
            field=models.ForeignKey(related_name='companionships', to='llts.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='companionship',
            field=models.ForeignKey(related_name='assignments', to='llts.Companionship'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='household',
            field=models.ForeignKey(to='llts.Household'),
            preserve_default=True,
        ),
    ]
