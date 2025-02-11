# Generated by Django 4.2 on 2024-07-29 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitioweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactoSitio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
                ('horario_atencion', models.CharField(max_length=200)),
                ('mapaurl', models.URLField(blank=True)),
                ('facebook_url', models.URLField(blank=True)),
                ('instagram_url', models.URLField(blank=True)),
                ('twitter_url', models.URLField(blank=True)),
                ('whatsapp_url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormularioContacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200)),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Inicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagenFondo', models.ImageField(blank=True, null=True, upload_to='inicio/')),
                ('imagenQuienesSomos', models.ImageField(blank=True, null=True, upload_to='inicioQuienesSomos/')),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('tituloProductos', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Nosotros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='nosotros/')),
                ('tituloElBorrachoFiel', models.CharField(max_length=200)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('imagenNosotros', models.ImageField(blank=True, null=True, upload_to='nosotros/')),
                ('valores', models.TextField()),
                ('equipo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('nombrepersona', models.CharField(max_length=200)),
            ],
        ),
    ]
