from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ["name"]

    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    class Meta:
        ordering = ["category"]
        verbose_name_plural = "articles"
        verbose_name = "article"

    title = models.CharField(max_length=350)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT, default=1, null=True)
    created = models.DateTimeField()
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
