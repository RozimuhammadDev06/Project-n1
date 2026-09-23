from django.db import models


TALIM = [
    ("yaxshi", "yaxshi"),
    ("orta", "orta"),
    ("yomon", "yomon"),
]


class Maktab(models.Model):
    number = models.IntegerField()
    honalar = models.IntegerField()
    elektronika = models.CharField(max_length=150)
    zona = models.CharField(max_length=300)
    talim = models.CharField(max_length=10, choices=TALIM)
    direktor = models.CharField(max_length=50)
    oqtuvchilar = models.IntegerField()
    oquvchilar = models.IntegerField()
    manzil = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.number}-maktab"


DAVOMAT_CHOICES = [
    ('KEL', 'KELDI'),
    ('KEM', 'KEMADI'),
    ('SAB', 'SABABLI'),
]


class Oquvchi(models.Model):
    alochilar_soni = models.IntegerField()
    ism_familiya = models.CharField(max_length=40)
    manzil = models.CharField(max_length=20)
    davomat = models.CharField(max_length=3, choices=DAVOMAT_CHOICES, default='KEL')

    def __str__(self):
        return self.ism_familiya

    
class Sinf(models.Model):
    nomi = models.CharField(max_length=50)
    dars_vaqti = models.CharField(max_length=50)
    sharoyit = models.CharField(max_length=100)
    xona_kengligi = models.PositiveIntegerField()
    yonalish = models.CharField(max_length=50)
    oqituvchi = models.CharField(max_length=25)
    oquvchilar = models.ForeignKey(Oquvchi, on_delete=models.CASCADE)
    orindiqlar = models.PositiveIntegerField()

    def __str__(self):
        return self.nomi

class new(models.Model):
    oquvchi = models.ForeignKey(Oquvchi, on_delete=models.CASCADE)