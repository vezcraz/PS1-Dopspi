# Generated by Django 2.2.1 on 2019-07-16 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year_Published', models.CharField(max_length=100)),
                ('Chapter_Number', models.CharField(max_length=100)),
                ('Table_Number', models.CharField(max_length=100)),
                ('Table_Content', models.CharField(max_length=200)),
                ('Excel_File', models.FileField(upload_to='')),
                ('Pdf_File', models.FileField(upload_to='')),
                ('graph', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Ext_Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year_Published', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('Icon', models.FileField(upload_to='')),
                ('Link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Index_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year_Published', models.CharField(max_length=100)),
                ('Chapter_Number', models.CharField(max_length=100)),
                ('Table_Content', models.TextField()),
                ('Color_Number', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year_Published', models.CharField(max_length=4)),
                ('Name', models.CharField(max_length=40)),
                ('Link', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Year_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year_Published', models.CharField(max_length=100)),
                ('Message', models.FileField(upload_to='')),
                ('front_cover', models.FileField(upload_to='')),
            ],
        ),
    ]
