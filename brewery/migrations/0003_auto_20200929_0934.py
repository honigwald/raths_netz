# Generated by Django 3.1.1 on 2020-09-29 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brewery', '0002_ingredient_step'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='amount',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='step',
            name='ingredient',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='brewery.ingredientstorage'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]
