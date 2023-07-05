from django.db import models

# Create your models here.

class location(models.Model):
    loc_id          = models.AutoField(primary_key=True)
    loc_name        = models.CharField(max_length=30)
    loc_limit       = models.IntegerField(default=0)
    loc_created     = models.DateTimeField(auto_now=True)

class ad(models.Model):
    ad_id           = models.AutoField(primary_key=True)
    ad_name         = models.TextField()
    ad_start        = models.DateField()
    ad_end          = models.DateField()
    ad_loc          = models.ForeignKey("location", on_delete=models.SET_NULL,null=True)
    ad_visits       = models.IntegerField(default=0)
    ad_created      = models.DateTimeField(auto_now=True)