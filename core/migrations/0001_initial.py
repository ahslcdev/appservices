# Generated by Django 3.2 on 2021-09-22 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('orcamento', models.CharField(max_length=255)),
                ('data_cadastro', models.DateField(auto_now_add=True)),
                ('data_limite', models.DateField()),
                ('situacao', models.CharField(choices=[('Aberto', 'Aberto'), ('Concluído', 'Concluído'), ('Cancelado', 'Cancelado')], max_length=255)),
                ('cometarios', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.service')),
            ],
        ),
    ]
