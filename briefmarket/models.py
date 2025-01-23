from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class IndividualInformation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{10,12}$')])
    email = models.EmailField()
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    class Meta:
        verbose_name = "اطلاعات فردی"
        verbose_name_plural = "اطلاعات فردی"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PurposeAdvertising(models.Model):
    short_team_goals = models.TextField()
    long_team_goals = models.TextField()
    current_media = models.TextField()
    desired_media = models.TextField()


class MarketShare(models.Model):
    marketing_share = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    strengths = models.TextField()
    weaknesses = models.TextField()


class BrandPosition(models.Model):
    company_position_short_term = models.TextField(null=True, blank=True)
    company_position_long_term = models.TextField(null=True, blank=True)
    competitors = models.JSONField(null=True, blank=True)  # To store multiple competitors as a list
    audience_environments = models.JSONField(null=True, blank=True)


class Target(models.Model):
    target_toman = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="تومان", default=0)
    target_dollar = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="دلار", default=0)
    target_euro = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="یورو", default=0)
    brand_book = models.TextField(blank=True)
    company_slogan = models.TextField(blank=True)
    target_audience = models.TextField(blank=True)


class Budget(models.Model):
    budget_toman = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="تومان", default=0)
    budget_dollar = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="دلار", default=0)
    budget_euro = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="یورو", default=0)

    MAIN_AUDIENCE_CHOICES = [
        ('children', 'Children'),
        ('youth', 'Youth'),
        ('adults', 'Adults'),
        ('elderly', 'Elderly'),
    ]
    main_audience = models.CharField(max_length=50, choices=MAIN_AUDIENCE_CHOICES, default='children')

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='male')

    ESTIMATED_REVENUE_CHOICES = [
        ('above_15m', 'Above 15m'),
        ('8_to_15m', '8 to 15m'),
        ('4_to_8m', '4 to 8m'),
        ('under_4m', 'Under 4m'),
    ]
    estimated_revenue = models.CharField(max_length=50, choices=ESTIMATED_REVENUE_CHOICES, default='under_4m')

    IMPORTANCE_SERVICE_CHOICES = [
        ('quality', 'Quality'),
        ('price', 'Price'),
        ('brand_name', 'Brand Name'),
        ('services', 'Services'),
        ('availability', 'Availability'),
        ('other', 'Other'),
    ]
    importance = models.CharField(max_length=50, choices=IMPORTANCE_SERVICE_CHOICES, default='quality')


class Request(models.Model):
    geographic_focus = models.CharField(max_length=50, choices=[('iran', 'Iran'), ('international', 'International')])
    audience_demographic = models.TextField()


def __str__(self):
    return f"{self.company_name} Brief Marketing"
