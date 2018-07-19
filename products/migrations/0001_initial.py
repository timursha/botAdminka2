# Generated by Django 2.0.6 on 2018-06-09 14:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=True, max_length=128, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Категория тикета',
                'verbose_name_plural': 'Категории тикетов',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=True, max_length=128, null=True)),
                ('username', models.CharField(blank=True, default=True, max_length=128, null=True)),
                ('town', models.CharField(blank=True, default=True, max_length=32, null=True)),
                ('phone', models.CharField(blank=True, default=True, max_length=68, null=True)),
                ('message', models.TextField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.status')),
            ],
            options={
                'verbose_name': 'Бланк',
                'verbose_name_plural': 'Бланки',
            },
        ),
        migrations.CreateModel(
            name='TicketCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=True, max_length=128, null=True)),
                ('is_main', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('Ticket', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Ticket')),
            ],
            options={
                'verbose_name': 'Категория тикета',
                'verbose_name_plural': 'Категории тикетов',
            },
        ),
    ]
