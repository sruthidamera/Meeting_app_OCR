# Generated by Django 4.1.7 on 2023-03-31 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=100)),
                ('person_name', models.CharField(max_length=100)),
                ('task_start_date', models.DateField()),
                ('task_end_date', models.DateField()),
                ('status', models.CharField(choices=[('todo', 'To Do'), ('inprogress', 'In Progress'), ('done', 'Done')], default='todo', max_length=20)),
            ],
        ),
    ]
