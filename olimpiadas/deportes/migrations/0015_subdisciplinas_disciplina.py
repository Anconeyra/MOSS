# Generated by Django 5.0.3 on 2024-07-26 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deportes', '0014_remove_categoria_descripcion_categoria_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdisciplinas',
            name='disciplina',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subdisciplinas', to='deportes.disciplinas'),
        ),
    ]
