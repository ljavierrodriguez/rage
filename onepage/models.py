from django.db import models


# Create your models here.
class General(models.Model):
    banner_home = models.ImageField(upload_to="banners")
    title_home = models.CharField(max_length=200)
    url_home = models.CharField(max_length=200)
    download_home = models.FileField(upload_to="download")
    title_about = models.CharField(max_length=200)
    description_about = models.TextField()
    download_about = models.FileField(upload_to="download")


class AboutDescription(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    active = models.BooleanField


class AboutProfileDescription(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
