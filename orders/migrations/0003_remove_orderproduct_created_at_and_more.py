# Generated by Django 5.0.6 on 2024-07-19 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20240624_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='ordered',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='product',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='product_price',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='product_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='product_title',
            field=models.CharField(default=0.0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='quantity',
            field=models.CharField(max_length=50),
        ),
    ]
