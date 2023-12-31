# Generated by Django 4.2.7 on 2023-11-25 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_alter_gradskacetvrt_broj'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gradskacetvrt',
            options={'verbose_name_plural': 'Gradske četvrti'},
        ),
        migrations.CreateModel(
            name='MjesniOdbor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=60, unique=True, verbose_name='Mjesni odbor')),
                ('address', models.CharField(blank=True, max_length=120, null=True, verbose_name='Adresa')),
                ('latitude', models.CharField(blank=True, max_length=200, null=True, verbose_name='Geo. širina')),
                ('longitude', models.CharField(blank=True, max_length=200, null=True, verbose_name='Geo. dužina')),
                ('gradska_cetvrt', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assets.gradskacetvrt', verbose_name='Gradska četvrt')),
            ],
            options={
                'verbose_name_plural': 'Mjesni odbori',
            },
        ),
    ]
