# Generated by Django 4.2.6 on 2023-11-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=100, unique=True, verbose_name='Nombre del cliente')),
                ('direccion_fiscal', models.CharField(default='', max_length=100, verbose_name='Direccion fiscal')),
                ('contacto_dir', models.CharField(default='', max_length=100, verbose_name='Contacto')),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='contenido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('hora_registro', models.TimeField(auto_now_add=True)),
                ('nombre_cliente', models.CharField(default='', max_length=100, verbose_name='Nombre del cliente')),
                ('direccion_fiscal', models.CharField(default='', max_length=100, verbose_name='Direccion fiscal')),
                ('contacto_dir', models.CharField(default='', max_length=100, verbose_name='Contacto')),
                ('empresa_transportadora', models.CharField(default='', max_length=100, verbose_name='Empresa transportadora')),
                ('nombre_transportista', models.CharField(default='', max_length=100, verbose_name='Nombre del transportista')),
                ('licencia', models.CharField(default='', max_length=100, verbose_name='No. de licencia')),
                ('certificado_fumigacion', models.CharField(default='', max_length=100, verbose_name='Certificado de fumigacion')),
                ('tracto_camion', models.CharField(default='', max_length=100, verbose_name='Tracto camion')),
                ('placas_unidad', models.CharField(default='', max_length=100, verbose_name='Placas de la unidad')),
                ('placas_caja', models.CharField(default='', max_length=100, verbose_name='Placas de la caja')),
                ('numero_caja', models.CharField(default='', max_length=100, verbose_name='No. Caja')),
                ('producto', models.CharField(default='', max_length=100, verbose_name='Producto')),
                ('cantidad_charolas', models.CharField(default='', max_length=100, verbose_name='Cantidad total de charolas')),
                ('numero_lote', models.CharField(default='', max_length=100, verbose_name='Numero de lote')),
                ('cantidad_tarimas', models.CharField(default='', max_length=100, verbose_name='Cantidad total de tarimas')),
                ('visual_paredes', models.ImageField(default='', upload_to='imagenes/', verbose_name='Paredes')),
                ('visual_piso', models.ImageField(default='', upload_to='imagenes/', verbose_name='Piso')),
                ('visual_techo', models.ImageField(default='', upload_to='imagenes/', verbose_name='Techo')),
                ('hora_llegada', models.CharField(default='', max_length=100, verbose_name='Hora de llegada')),
                ('hora_salida', models.CharField(default='', max_length=100, verbose_name='Hora de salida')),
                ('visual_tarima1', models.ImageField(default='', upload_to='imagenes/', verbose_name='Primer tarima')),
                ('visual_mitad_carga', models.ImageField(default='', upload_to='imagenes/', verbose_name='Mitad de carga')),
                ('visual_fin_carga', models.ImageField(default='', upload_to='imagenes/', verbose_name='Fin de carga')),
                ('visual_cerrado_unidad', models.ImageField(default='', upload_to='imagenes/', verbose_name='Cerrado de la unidad')),
                ('hora_inicio_carga', models.CharField(default='', max_length=100, verbose_name='Hora inicio de carga')),
                ('hora_fin_carga', models.CharField(default='', max_length=100, verbose_name='Hora fin de carga')),
            ],
            options={
                'verbose_name': 'contenido',
                'verbose_name_plural': 'contenidos',
            },
        ),
    ]
