# Generated by Django 2.1a1 on 2018-05-20 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('accountingApp', '0006_accountingbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('balance', models.FloatField()),
                ('accounting_book',
                 models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accountingApp.AccountingBook')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amout', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account',
                 models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accountingApp.Account')),
            ],
        ),
    ]