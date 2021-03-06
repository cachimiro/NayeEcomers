# Generated by Django 2.2 on 2020-04-16 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200416_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('I', 'info'), ('S', 'secondary'), ('D', 'danger')], default='I', max_length=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='core.OrderItem'),
        ),
        migrations.AlterField(
            model_name='refund',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Order'),
        ),
    ]
