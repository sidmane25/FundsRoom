# myapp/models.py

from django.db import models

class UserProfile(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    preferred_style = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id

class ShoppingHistory(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user_id} - {self.item_name}"
