# Generated by Django 2.1.2 on 2019-02-20 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20181026_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.CharField(choices=[('build_group', '开发团队招募'), ('programing', '开发任务'), ('knowledge_communication', '知识交流'), ('tutor', '家教'), ('others', '其它')], max_length=32),
        ),
    ]
