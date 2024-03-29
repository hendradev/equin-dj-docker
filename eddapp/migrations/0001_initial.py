# Generated by Django 3.1.6 on 2021-02-20 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pekerjaan',
            fields=[
                ('idpemberikerjapekerjaan', models.AutoField(primary_key=True, serialize=False)),
                ('namapekerjaan', models.CharField(blank=True, max_length=255, null=True)),
                ('gaji', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pemberikerja_pekerjaan',
            },
        ),
        migrations.CreateModel(
            name='PelamarKerja',
            fields=[
                ('idpelamarkerja', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('alamat', models.CharField(blank=True, max_length=255, null=True)),
                ('skill', models.CharField(blank=True, max_length=255, null=True)),
                ('pendidikan_terakhir', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'pelamarkerja',
            },
        ),
        migrations.CreateModel(
            name='PemberiKerja',
            fields=[
                ('idpemberikerja', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('perusahaan', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'pemberikerja',
            },
        ),
        migrations.CreateModel(
            name='PekerjaanPelamarKerja',
            fields=[
                ('idpemberikerjapekerjaanpelamarkerja', models.AutoField(primary_key=True, serialize=False)),
                ('tanggal_melamar', models.DateTimeField(blank=True, null=True)),
                ('cover_letter', models.TextField(blank=True, null=True)),
                ('gaji_yang_diminta', models.IntegerField(blank=True, null=True)),
                ('id_pelamarkerja', models.ForeignKey(blank=True, db_column='id_pelamarkerja', null=True, on_delete=django.db.models.deletion.CASCADE, to='eddapp.pelamarkerja')),
                ('id_pemberikerja_pekerjaan', models.ForeignKey(blank=True, db_column='id_pemberikerja_pekerjaan', null=True, on_delete=django.db.models.deletion.CASCADE, to='eddapp.pekerjaan')),
            ],
            options={
                'db_table': 'pemberikerja_pekerjaan_pelamarkerja',
            },
        ),
        migrations.AddField(
            model_name='pekerjaan',
            name='id_pemberikerja',
            field=models.ForeignKey(blank=True, db_column='id_pemberikerja', null=True, on_delete=django.db.models.deletion.CASCADE, to='eddapp.pemberikerja'),
        ),
    ]
