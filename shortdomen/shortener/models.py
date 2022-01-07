from django.db import models
from django.contrib.auth import get_user_model
from .utils import short
from django.contrib.auth.models import User as U

User = get_user_model()


class Domain(models.Model):
    link = models.URLField(unique=True)
    short_link = models.URLField(blank=True, max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Оригинальная ссылка:{self.link} - Укороченная ссылка:{self.short_link}'


    def save(self, *args, **kwargs):
        if not self.short_link:
            self.short_link = short(self.link)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-pub_date']
