# Generated by Django 5.1.3 on 2025-01-01 10:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('briefmarket', '0003_rename_dollar_marketingbrief_budget_dollar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_position_short_term', models.TextField(blank=True, null=True)),
                ('company_position_long_term', models.TextField(blank=True, null=True)),
                ('competitors', models.JSONField(blank=True, null=True)),
                ('audience_environments', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_toman', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='تومان')),
                ('budget_dollar', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='دلار')),
                ('budget_euro', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='یورو')),
                ('main_audience', models.CharField(choices=[('children', 'Children'), ('youth', 'Youth'), ('adults', 'Adults'), ('elderly', 'Elderly')], default='children', max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=50)),
                ('estimated_revenue', models.CharField(choices=[('above_15m', 'Above 15m'), ('8_to_15m', '8 to 15m'), ('4_to_8m', '4 to 8m'), ('under_4m', 'Under 4m')], default='under_4m', max_length=50)),
                ('importance', models.CharField(choices=[('quality', 'Quality'), ('price', 'Price'), ('brand_name', 'Brand Name'), ('services', 'Services'), ('availability', 'Availability'), ('other', 'Other')], default='quality', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IndividualInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^\\d{10,12}$')])),
                ('email', models.EmailField(max_length=254)),
                ('company_name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'اطلاعات فردی',
                'verbose_name_plural': 'اطلاعات فردی',
            },
        ),
        migrations.CreateModel(
            name='MarketShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marketing_share', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('strengths', models.TextField()),
                ('weaknesses', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PurposeAdvertising',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_team_goals', models.TextField()),
                ('long_team_goals', models.TextField()),
                ('current_media', models.TextField()),
                ('desired_media', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geographic_focus', models.CharField(choices=[('iran', 'Iran'), ('international', 'International')], max_length=50)),
                ('audience_demographic', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_toman', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='تومان')),
                ('target_dollar', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='دلار')),
                ('target_euro', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='یورو')),
                ('brand_book', models.TextField(blank=True)),
                ('company_slogan', models.TextField(blank=True)),
                ('target_audience', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='MarketingBrief',
        ),
    ]
