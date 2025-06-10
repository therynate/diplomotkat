from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ('sell', 'Продать технику'),
        ('repair', 'Ремонт техники'),
        ('buy', 'Купить б/у технику'),
        ('build_pc', 'Сборка ПК'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='service_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending', choices=[
        ('pending', 'На рассмотрении'),
        ('accepted', 'Принята'),
        ('rejected', 'Отклонена'),
    ])

    class Meta:
        verbose_name = 'Заявку на услугу'
        verbose_name_plural = 'Заявки на услугу'

    def __str__(self):
        return f"{self.get_service_type_display()} - {self.title}"


class UsedDevice(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='used_devices/')
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Б/У устройства'
        verbose_name_plural = 'Б/У устройства'

    def __str__(self):
        return self.name


class PrebuiltPC(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='prebuilt_pcs/')
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Готовый ПК'
        verbose_name_plural = 'Готовые ПК'

    def __str__(self):
        return self.name