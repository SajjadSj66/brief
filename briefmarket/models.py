from django.db import models


# Create your models here.
class MarketingBrief(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    short_team_goals = models.TextField()
    long_team_goals = models.TextField()
    current_media = models.TextField()
    desired_media = models.TextField()
    marketing_share = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    strengths = models.TextField()
    weaknesses = models.TextField()
    company_position_short_term = models.TextField()
    company_position_long_term = models.TextField()
    competitors = models.JSONField()  # To store multiple competitors as a list
    audience_environments = models.JSONField()
    toman = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="تومان")
    dollar = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="دلار")
    euro = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="یورو")
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    audience_demographic = models.TextField()
    geographic_focus = models.CharField(max_length=50, choices=[('iran', 'Iran'), ('international', 'International')])

    def __str__(self):
        return f"{self.company_name} Brief Marketing"
