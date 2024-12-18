# Generated by Django 5.1.3 on 2024-11-14 18:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0001_initial'),
        ('warehouse', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.machine')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.product')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='production_entries', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
