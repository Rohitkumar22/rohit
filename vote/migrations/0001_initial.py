# Generated by Django 2.1.1 on 2019-10-06 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_txt', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question_txt', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.Food'),
        ),
    ]
