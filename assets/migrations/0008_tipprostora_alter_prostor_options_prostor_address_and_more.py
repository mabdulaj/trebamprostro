# Generated by Django 4.2.7 on 2023-11-25 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_alter_grad_ime_grada_alter_gradskacetvrt_grad_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipProstora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=60, unique=True, verbose_name='Tip prostora')),
            ],
            options={
                'verbose_name_plural': 'Tipovi prostora',
            },
        ),
        migrations.AlterModelOptions(
            name='prostor',
            options={'verbose_name_plural': 'Prostori'},
        ),
        migrations.AddField(
            model_name='prostor',
            name='address',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Adresa prostora'),
        ),
        migrations.AddField(
            model_name='prostor',
            name='grijanje',
            field=models.BooleanField(default=False, verbose_name='Grijanje'),
        ),
        migrations.AddField(
            model_name='prostor',
            name='img1',
            field=models.ImageField(blank=True, default='0_Home_Black.png', null=True, upload_to='slike', verbose_name='Slike'),
        ),
        migrations.AddField(
            model_name='prostor',
            name='img2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='slike', verbose_name='Slike'),
        ),
        migrations.AddField(
            model_name='prostor',
            name='img3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='slike', verbose_name='Slike'),
        ),
        migrations.AddField(
            model_name='prostor',
            name='img4',
            field=models.ImageField(blank=True, default='', null=True, upload_to='slike', verbose_name='Slike'),
        ),
        migrations.AddField(
            model_name='prostor',
            name='klima',
            field=models.BooleanField(default=False, verbose_name='Klima'),
        ),
        migrations.AddField(
            model_name='prostor',
            name='latitude',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Geo. širina'),
        ),
        migrations.AddField(
            model_name='prostor',
            name='longitude',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Geo. dužina'),
        ),
        migrations.AddField(
            model_name='prostor',
            name='mjesniodbor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='assets.mjesniodbor', verbose_name='Mjesni odbor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prostor',
            name='povrsina',
            field=models.FloatField(default=0.0, verbose_name='Površina [m2]'),
        ),
        migrations.AddField(
            model_name='prostor',
            name='sanitarni',
            field=models.BooleanField(default=False, verbose_name='Sanitarni čvor'),
        ),
        migrations.AddField(
            model_name='prostor',
            name='wifi',
            field=models.BooleanField(default=False, verbose_name='WiFi'),
        ),
        migrations.AlterField(
            model_name='mjesniodbor',
            name='broj',
            field=models.IntegerField(verbose_name='Broj mjesnog odbora'),
        ),
        migrations.AddField(
            model_name='prostor',
            name='tipprostora',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='assets.tipprostora', verbose_name='Tip prostora'),
            preserve_default=False,
        ),
    ]