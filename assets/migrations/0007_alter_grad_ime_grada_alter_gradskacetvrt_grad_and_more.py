# Generated by Django 4.2.7 on 2023-11-25 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_alter_grad_ime_grada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grad',
            name='ime_grada',
            field=models.CharField(max_length=60, unique=True, verbose_name='Grad'),
        ),
        migrations.AlterField(
            model_name='gradskacetvrt',
            name='grad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.grad', verbose_name='Grad'),
        ),
        migrations.AlterField(
            model_name='mjesniodbor',
            name='gradska_cetvrt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.gradskacetvrt', verbose_name='Gradska četvrt'),
        ),
    ]
