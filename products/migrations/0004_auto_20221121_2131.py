# Generated by Django 3.2.13 on 2022-11-21 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_저장용량'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='GPU종류등급',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='가격등급',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='무게등급',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='저장용량등급',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='화면크기등급',
            field=models.TextField(blank=True, null=True),
        ),
    ]