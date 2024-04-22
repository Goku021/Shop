from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_category")
    description = models.TextField()
    price = models.DecimalField(max_digits=25, decimal_places=2)
    image = models.ImageField(upload_to="images/")
    created = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['id', 'created'])
        ]
