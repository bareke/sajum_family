# Generated by Django 3.0.3 on 2020-02-10 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adjunt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_1', models.CharField(max_length=45)),
                ('name_2', models.CharField(max_length=45)),
                ('lastname_1', models.CharField(max_length=45)),
                ('lastname_2', models.CharField(max_length=45)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('actor', models.CharField(choices=[('DENUNCIANTE', 'Denunciante'), ('AGRESOR', 'Agresor'), ('VICTIMA', 'Victima'), ('ACUDIENTE', 'Acuediente')], max_length=45)),
                ('document_type', models.CharField(choices=[('NUIP', 'nuip'), ('T.I', 't.i.'), ('C.C', 'c.c.'), ('C.E.', 'c.e.'), ('SIN IDENTIFICACION', 'Sin identificación'), ('NIT', 'nit')], max_length=45)),
                ('identification', models.IntegerField()),
                ('date_birth', models.DateField()),
                ('health', models.CharField(choices=[('NUIP', 'nuip'), ('T.I', 't.i.'), ('C.C', 'c.c.'), ('C.E.', 'c.e.'), ('SIN IDENTIFICACION', 'Sin identificación'), ('NIT', 'nit')], max_length=45)),
                ('eps', models.BooleanField(default=False)),
                ('occupation', models.CharField(max_length=45)),
                ('gender', models.CharField(choices=[('NUIP', 'nuip'), ('T.I', 't.i.'), ('C.C', 'c.c.'), ('C.E.', 'c.e.'), ('SIN IDENTIFICACION', 'Sin identificación'), ('NIT', 'nit')], max_length=45)),
                ('marital_status', models.CharField(choices=[('SOLTERO', 'Soltero'), ('CASADO', 'Casado'), ('UNION LIBRE', 'Union libre'), ('UNION DE HECHO', 'Union de hecho'), ('SEPARADO', 'Separado'), ('DIVORCIADO', 'Divorciado'), ('VIUDO', 'Viudo'), ('NOVIAZGO', 'Noviazgo')], max_length=45)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('institute', models.CharField(blank=True, max_length=45, null=True)),
                ('workday', models.CharField(choices=[('DIURNA', 'Diurna'), ('TARDE', 'Tarde'), ('NOCTURNA', 'Nocturna')], max_length=45)),
                ('education', models.CharField(choices=[('PRIMARIA', 'Primaria'), ('POSTGRADO', 'Postgrado'), ('SUPERIOR', 'Superior'), ('ANALFABETA', 'Analfabeta'), ('PREESCOLAR', 'Preescolar'), ('SECUNDARIA', 'Secundaria')], max_length=45)),
                ('head_family', models.BooleanField(blank=True, null=True)),
                ('pregnant', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=45)),
                ('denounced', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='denounceds', to='complaint.Citizen')),
                ('hostess', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hostess', to='complaint.Citizen')),
                ('victim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='victims', to='complaint.Citizen')),
                ('whistleblower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whistleblowers', to='complaint.Citizen')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipalities', to='complaint.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_1', models.CharField(max_length=45)),
                ('name_2', models.CharField(max_length=45)),
                ('lastname_1', models.CharField(max_length=45)),
                ('lastname_2', models.CharField(max_length=45)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('profession', models.CharField(max_length=45)),
                ('position', models.CharField(max_length=45)),
                ('municipality', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='officer', to='complaint.Municipality')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkOrden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('study', models.CharField(max_length=45)),
                ('officer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='work_orden', to='complaint.Officer')),
            ],
        ),
        migrations.CreateModel(
            name='Vereda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('municipality', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vereda', to='complaint.Municipality')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('proceedings', models.CharField(max_length=45)),
                ('reason', models.TextField()),
                ('adjunts', models.ManyToManyField(to='complaint.Adjunt')),
                ('municipality', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='transfer', to='complaint.Municipality')),
            ],
        ),
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('citizen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telephones', to='complaint.Citizen')),
                ('officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telephones', to='complaint.Officer')),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('citizen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationships', to='complaint.Citizen')),
            ],
        ),
        migrations.AddField(
            model_name='officer',
            name='vereda',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='officer', to='complaint.Vereda'),
        ),
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('facts', models.TextField()),
                ('pretension', models.CharField(max_length=45)),
                ('complaints', models.ManyToManyField(to='complaint.Complaint')),
                ('municipality', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fact', to='complaint.Municipality')),
                ('vereda', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fact', to='complaint.Vereda')),
            ],
        ),
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('citizen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ethnicities', to='complaint.Citizen')),
            ],
            options={
                'verbose_name_plural': 'ethnicities',
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.IntegerField()),
                ('name', models.CharField(max_length=45)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('principal', models.CharField(max_length=45)),
                ('url_web_site', models.CharField(max_length=45)),
                ('slogan', models.CharField(max_length=45)),
                ('url_icon', models.CharField(max_length=100)),
                ('municipality', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='entity', to='complaint.Municipality')),
                ('telephone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='complaint.Telephone')),
            ],
            options={
                'verbose_name_plural': 'entities',
            },
        ),
        migrations.CreateModel(
            name='Disability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('citizen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disabilities', to='complaint.Citizen')),
            ],
            options={
                'verbose_name_plural': 'disabilities',
            },
        ),
        migrations.AddField(
            model_name='citizen',
            name='department_expedition',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='citizen', to='complaint.Department'),
        ),
        migrations.AddField(
            model_name='citizen',
            name='municipality',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='citizen', to='complaint.Municipality'),
        ),
        migrations.AddField(
            model_name='citizen',
            name='vereda',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='citizen', to='complaint.Vereda'),
        ),
        migrations.AddField(
            model_name='adjunt',
            name='citizen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adjunts', to='complaint.Citizen'),
        ),
        migrations.AddField(
            model_name='adjunt',
            name='fact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adjunts', to='complaint.Fact'),
        ),
        migrations.AddField(
            model_name='adjunt',
            name='work_orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adjunts', to='complaint.WorkOrden'),
        ),
    ]
