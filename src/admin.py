from django.contrib import admin

from src.models import Maktab,Sinf

# Register your models here.


@admin.register(Maktab)
class MaktabAdmin(admin.ModelAdmin):
    list_display = ( "number", "honalar", "elektronika", "zona", "talim", "direktor", "oqtuvchilar", "oquvchilar", "manzil")
    search_fields = ("number", "direktor")
    list_filter = ("talim",)


@admin.register(Sinf)
class SinfAdmin(admin.ModelAdmin):
    list_display = ("nomi", "dars_vaqti", "sharoyit", "xona_kengligi", "yonalish", "oqituvchi", "oquvchilar", "orindiqlar")
    search_fields = ("nomi", "oqituvchi")
    list_filter = ("yonalish",)