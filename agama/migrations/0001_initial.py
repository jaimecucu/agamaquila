# Generated by Django 4.2.6 on 2023-11-24 13:52

from django.db import migrations, models
import django.db.models.deletion


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
                ('sin_hoyos', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('sin_parches', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('sin_salientes', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('sin_laminas', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('puertas_empaques', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('puertas_hermetico', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('puertas_salientes', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('puertas_laminas', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('higiene_limpios', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('higiene_olores', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('higiene_plagas', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('paredes_hoyos', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('paredes_parches', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('paredes_salientes', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('paredes_laminas', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('techos_hoyos', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('techos_salientes', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('techos_laminas', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('externas_llantas', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('externas_refaccion', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('externas_patines', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('externas_luces', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('externas_tanque', models.CharField(default='', max_length=10, verbose_name='Charolas')),
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
        migrations.CreateModel(
            name='contenido2',
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
                ('sin_hoyos', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('sin_parches', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('sin_salientes', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('sin_laminas', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('puertas_empaques', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('puertas_hermetico', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('puertas_salientes', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('puertas_laminas', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('higiene_limpios', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('higiene_olores', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('higiene_plagas', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('paredes_hoyos', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('paredes_parches', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('paredes_salientes', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('paredes_laminas', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('techos_hoyos', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('techos_salientes', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('techos_laminas', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('externas_llantas', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('externas_refaccion', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('externas_patines', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('externas_luces', models.CharField(default='', max_length=10, verbose_name='Charolas')),
                ('externas_tanque', models.CharField(default='', max_length=10, verbose_name='Charolas')),
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
                'verbose_name': 'contenido2',
                'verbose_name_plural': 'contenidos2',
            },
        ),
        migrations.CreateModel(
            name='Tarima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_tarima', models.IntegerField(verbose_name='Numero de Tarima')),
                ('lote_tarima', models.CharField(default='', max_length=50, verbose_name='Numero de lote')),
                ('producto_tarima', models.CharField(default='', max_length=150, verbose_name='Producto')),
                ('camas_tarima', models.IntegerField(verbose_name='Numero de camas')),
                ('paquetes_tarima', models.IntegerField(verbose_name='Numero de paquetes')),
                ('latas_tarima', models.CharField(default='', max_length=5, verbose_name='Lata')),
                ('charolas_tarima', models.CharField(default='', max_length=5, verbose_name='Charolas')),
                ('emplayado_tarima', models.CharField(default='', max_length=5, verbose_name='Emplayado')),
                ('observaciones_tarima', models.CharField(default='', max_length=200, verbose_name='Observaciones')),
            ],
            options={
                'verbose_name': 'Tarima',
                'verbose_name_plural': 'Tarimas',
            },
        ),
        migrations.CreateModel(
            name='Tarima2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_tarima', models.IntegerField(verbose_name='Numero de Tarima')),
                ('lote_tarima', models.CharField(default='', max_length=50, verbose_name='Numero de lote')),
                ('producto_tarima', models.CharField(default='', max_length=150, verbose_name='Producto')),
                ('camas_tarima', models.IntegerField(verbose_name='Numero de camas')),
                ('paquetes_tarima', models.IntegerField(verbose_name='Numero de paquetes')),
                ('latas_tarima', models.CharField(default='', max_length=5, verbose_name='Lata')),
                ('charolas_tarima', models.CharField(default='', max_length=5, verbose_name='Charolas')),
                ('emplayado_tarima', models.CharField(default='', max_length=5, verbose_name='Emplayado')),
                ('observaciones_tarima', models.CharField(default='', max_length=200, verbose_name='Observaciones')),
                ('contenido2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agama.contenido2')),
            ],
            options={
                'verbose_name': 'Tarima2',
                'verbose_name_plural': 'Tarimas2',
            },
        ),
    ]
