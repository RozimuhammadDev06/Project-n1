from django.contrib import admin
from .models import Maktab, Oquvchi, Sinf


@admin.register(Maktab)
class MaktabAdmin(admin.ModelAdmin):
    list_display = ('number', 'direktor', 'oqtuvchilar', 'oquvchilar', 'talim', 'zona', 'manzil')
    list_filter = ('talim', 'zona')
    search_fields = ('number', 'direktor', 'manzil', 'zona')
    ordering = ('number',)


@admin.register(Oquvchi)
class OquvchiAdmin(admin.ModelAdmin):
    list_display = ('ism_familiya', 'manzil', 'davomat', 'alochilar_soni')
    list_filter = ('davomat',)
    search_fields = ('ism_familiya', 'manzil')
    ordering = ('ism_familiya',)


@admin.register(Sinf)
class SinfAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'oqituvchi', 'dars_vaqti', 'yonalish', 'orindiqlar', 'xona_kengligi')
    list_filter = ('yonalish',)
    search_fields = ('nomi', 'oqituvchi', 'yonalish')
    ordering = ('nomi',)
