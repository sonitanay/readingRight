from django.db import models

# Create your models here.

class GItem(models.Model):
    user = models.CharField(max_length=120, null=True)
    item_name = models.CharField(max_length=120)
    item_qty = models.IntegerField()
    item_status = models.TextField()
    item_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.item_name