from django.db import models
from django_outbox_pattern.decorators import Config
from django_outbox_pattern.decorators import publish


@publish([Config(destination='/exchange/saga/stock', version="v1")])
class Inventory(models.Model):
    product_id = models.AutoField(primary_key=True)
    quantity_available = models.PositiveIntegerField(default=0)
    reserved_quantity = models.PositiveIntegerField(default=0)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Product {self.product_id} - Available: {self.quantity_available}, Reserved: {self.reserved_quantity}"
