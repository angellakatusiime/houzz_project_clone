from django.db import models

# Create your models here.
class cart(models.Model):
     item_id = models.IntegerField(default=0,null=False)
     product = models.CharField(max_length=70,null=False)
     quantity = models.IntegerField(default='none',null=False)
     price = models.IntegerField(default='none',null=False)

     def __str__(self):
          return self.product
   