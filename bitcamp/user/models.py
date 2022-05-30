from django.db import models
from django.urls import reverse
# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from sqlalchemy import null


class Author(User):
    image = models.ImageField(upload_to='profiles', blank=True, null=True)

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse('user:author', kwargs={'pk':self.pk})

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')