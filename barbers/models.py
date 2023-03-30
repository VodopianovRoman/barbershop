from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Barbers(models.Model):
    barber_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    barber_surname = models.CharField(max_length=64, blank=True, null=True, default=None)
    barber_phone = models.IntegerField(max_length=16, blank=True, null=True, default=None)
    barber_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'Barber: {self.id}, {self.barber_surname}, {self.is_active}'

    class Meta:
        verbose_name = 'Барбер'
        verbose_name_plural = 'Барбери'


class BarberFoto(models.Model):
    barber = models.ForeignKey(Barbers, blank=True, null=True, default=None, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='barbers_foto')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Фото барбера'
        verbose_name_plural = 'Фото барберів'