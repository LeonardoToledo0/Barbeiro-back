# Generated by Django 5.0.2 on 2024-02-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_reserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('imagem1', models.ImageField(blank=True, null=True, upload_to='galeria/')),
                ('imagem2', models.ImageField(blank=True, null=True, upload_to='galeria/')),
                ('imagem3', models.ImageField(blank=True, null=True, upload_to='galeria/')),
            ],
        ),
    ]