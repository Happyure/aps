# Generated by Django 4.1.1 on 2022-10-05 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dokter',
            fields=[
                ('iddokter', models.AutoField(primary_key=True, serialize=False)),
                ('namadokter', models.CharField(max_length=50)),
                ('nohpdokter', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pasien',
            fields=[
                ('idpasien', models.AutoField(primary_key=True, serialize=False)),
                ('namapasien', models.CharField(max_length=50)),
                ('jeniskelaminpasien', models.CharField(max_length=15)),
                ('tanggallahir', models.DateField()),
                ('nohppasien', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pelayanan',
            fields=[
                ('idpelayanan', models.AutoField(primary_key=True, serialize=False)),
                ('jenispelayanan', models.CharField(max_length=50)),
                ('hargapelayanan', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pendaftaran',
            fields=[
                ('idpendaftaran', models.AutoField(primary_key=True, serialize=False)),
                ('tanggalpendaftaran', models.DateField()),
                ('iddokter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dokter')),
                ('idpasien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pasien')),
            ],
        ),
        migrations.CreateModel(
            name='detailpelayanan',
            fields=[
                ('iddetailpelayanan', models.AutoField(primary_key=True, serialize=False)),
                ('jumlahjenispelayanan', models.IntegerField()),
                ('idpelayanan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pelayanan')),
                ('idpendaftaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pendaftaran')),
            ],
        ),
    ]
