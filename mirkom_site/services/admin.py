from django.contrib import admin
from .models import ServiceRequest, UsedDevice, PrebuiltPC
from django.utils.translation import gettext_lazy as _

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'service_type', 'title', 'status')
    list_filter = ('service_type', 'status')
    search_fields = ('title', 'description')

    # Русские названия полей
    fieldsets = (
        (_('Основная информация'), {
            'fields': ('user', 'service_type', 'title', 'description')
        }),
        (_('Дополнительно'), {
            'fields': ('photo', 'status', 'created_at')
        }),
    )

    # Русские названия в списке
    def service_type(self, obj):
        service_types = {
            'sell': 'Продать технику',
            'repair': 'Ремонт техники',
            'buy': 'Купить б/у технику',
            'build_pc': 'Сборка ПК'
        }
        return service_types.get(obj.service_type, obj.service_type)
    service_type.short_description = 'Тип услуги'


    def status(self, obj):
        statuses = {
            'pending': 'На рассмотрении',
            'accepted': 'Принята',
            'rejected': 'Отклонена'
        }
        return statuses.get(obj.status, obj.status)
    status.short_description = 'Статус'

@admin.register(UsedDevice)
class UsedDeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    search_fields = ('name', 'description')
    list_filter = ('is_available',)

    # Русские названия
    fieldsets = (
        (_('Информация о технике'), {
            'fields': ('name', 'description', 'price')
        }),
        (_('Изображение и доступность'), {
            'fields': ('photo', 'is_available')
        }),
    )

    def is_available(self, obj):
        return 'Да' if obj.is_available else 'Нет'
    is_available.short_description = 'Доступно'
    is_available.boolean = True


@admin.register(PrebuiltPC)
class PrebuiltPCAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    search_fields = ('name', 'description')
    list_filter = ('is_available',)

    # Русские названия
    fieldsets = (
        (_('Характеристики ПК'), {
            'fields': ('name', 'description', 'price')
        }),
        (_('Изображение и доступность'), {
            'fields': ('photo', 'is_available')
        }),
    )

    def is_available(self, obj):
        return 'Да' if obj.is_available else 'Нет'
    is_available.short_description = 'Доступно'
    is_available.boolean = True