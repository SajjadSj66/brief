# Generated by Django 5.1.3 on 2024-12-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('briefmarket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketingbrief',
            name='audience_environments',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='marketingbrief',
            name='company_position_long_term',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='marketingbrief',
            name='company_position_short_term',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='marketingbrief',
            name='competitors',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='marketingbrief',
            name='dollar',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='دلار'),
        ),
        migrations.AddField(
            model_name='marketingbrief',
            name='euro',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='یورو'),
        ),
        migrations.AddField(
            model_name='marketingbrief',
            name='toman',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='تومان'),
        ),
    ]
