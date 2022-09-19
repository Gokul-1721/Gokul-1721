from django.db import models

class Category(models.Model):
    categoryname=models.CharField(max_length=200)

    def __str__(self):
        return self.categoryname

class Product(models.Model):
    productname=models.CharField(max_length=200)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    description=models.TextField()
    image=models.URLField()
    stars=models.IntegerField(null=True)
    status=models.BooleanField(default=True)

    def __str__(self) -> str:
        return (self.productname)




