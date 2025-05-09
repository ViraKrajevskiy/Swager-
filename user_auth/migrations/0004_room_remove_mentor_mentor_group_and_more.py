# Generated by Django 5.2 on 2025-04-14 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0003_remove_course_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ed', models.DateField(auto_now_add=True)),
                ('updated_ed', models.DateField(auto_now=True)),
                ('rom_num', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='mentor_group',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='teacher_group',
        ),
        migrations.AddField(
            model_name='lesson',
            name='rom_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_auth.room'),
        ),
    ]
