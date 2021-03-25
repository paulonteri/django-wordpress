from django.db import models


class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    taxonomy = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.id}: {self.slug}"


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    taxonomy = models.CharField(max_length=255, null=True, blank=True)
    parent = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}: {self.slug}"
