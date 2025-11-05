from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import random
import string

class URL(models.Model):
    original_url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    
    # Short Link Generator
    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(6))
    
    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.generate_short_code()

        if not self.expiration_date:
            self.expiration_date = timezone.now() + timedelta(days=30)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.original_url} -> {self.short_code}"

class Click(models.Model):
    url = models.ForeignKey(URL, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    clicked_at = models.DateTimeField(auto_now_add=True)
    user_agent = models.TextField(null=True, blank=True)