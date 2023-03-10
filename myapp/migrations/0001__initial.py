# Generated by Django 4.0.4 on 2022-11-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NLP_models',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model_name', models.CharField(max_length=45)),
                ('model_task', models.CharField(max_length=45)),
                ('epoch', models.IntegerField()),
                ('batch_size', models.IntegerField()),
                ('learning_rate', models.DecimalField(decimal_places=5, max_digits=20)),
                ('precision', models.DecimalField(decimal_places=3, max_digits=20)),
                ('recall', models.DecimalField(decimal_places=3, max_digits=20)),
                ('f1', models.DecimalField(decimal_places=3, max_digits=20)),
                ('volume', models.DecimalField(decimal_places=3, max_digits=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(help_text='ex) pretrained-model, used data-set etc...')),
            ],
            options={
                'db_table': 'NLP_Models',
            },
        ),
    ]
