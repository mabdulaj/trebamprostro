from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Grad(models.Model):
    ime_grada = models.CharField(max_length=60, unique=True, verbose_name= 'Grad')
    zipcode = models.CharField(max_length=10, blank=True, null=True, verbose_name= 'Poštanski broj')
    drzava = models.CharField(max_length=30, verbose_name= 'Država')
    latitude = models.CharField(max_length=200, blank=True, null=True, verbose_name= 'Geo. širina')
    longitude = models.CharField(max_length=200, blank=True, null=True, verbose_name= 'Geo. dužina')

    def __str__(self):
        return self.ime_grada

    class Meta:
        verbose_name_plural = 'Gradovi'

class GradskaCetvrt(models.Model):
    ime = models.CharField(max_length=60, verbose_name='Gradska četvrt')
    grad = models.ForeignKey(Grad, on_delete=models.CASCADE, verbose_name='Grad')

    def __str__(self):
        return self.ime

    class Meta:
        verbose_name_plural = 'Gradske četvrti'

class MjesniOdbor(models.Model):
    ime = models.CharField(max_length=60, unique=True, verbose_name= 'Mjesni odbor')
    broj = models.IntegerField(verbose_name='Broj mjesnog odbora')
    address = models.CharField(max_length=120, blank=True, null=True, verbose_name='Adresa')
    gradska_cetvrt = models.ForeignKey(GradskaCetvrt, on_delete=models.CASCADE, verbose_name='Gradska četvrt')
    latitude = models.CharField(max_length=200, blank=True, null=True, verbose_name= 'Geo. širina')
    longitude = models.CharField(max_length=200, blank=True, null=True, verbose_name= 'Geo. dužina')

    def __str__(self):
        return (str(self.ime))

    class Meta:
        verbose_name_plural = 'Mjesni odbori'

class TipProstora(models.Model):
    ime = models.CharField(max_length=60, unique=True, verbose_name= 'Tip prostora')

    def __str__(self):
        return (self.ime)

    class Meta:
        verbose_name_plural = 'Tipovi prostora'


class Prostor(models.Model):
    ime = models.CharField(max_length=60, verbose_name= 'Naziv')
    tipprostora = models.ForeignKey(TipProstora, on_delete=models.CASCADE, verbose_name='Tip prostora')
    povrsina = models.FloatField(default=0.0, verbose_name='Površina [m2]')
    mjesniodbor = models.ForeignKey(MjesniOdbor, on_delete=models.CASCADE, verbose_name='Mjesni odbor')
    address = models.CharField(max_length=120, blank=True, null=True, verbose_name='Adresa prostora')
    latitude = models.CharField(max_length=200, blank=True, null=True, verbose_name= 'Geo. širina')
    longitude = models.CharField(max_length=200, blank=True, null=True, verbose_name= 'Geo. dužina')
    sanitarni = models.BooleanField(default=False, verbose_name= 'Sanitarni čvor')
    grijanje = models.BooleanField(default=False, verbose_name='Grijanje')
    klima = models.BooleanField(default=False, verbose_name='Klima')
    wifi = models.BooleanField(default=False, verbose_name='WiFi')

    img1 = models.ImageField(default='0_Home_Black.png', upload_to='slike', blank=True, null=True,
                               verbose_name='Slike')
    img2 = models.ImageField(upload_to='slike', blank=True, null=True,
                               verbose_name='Slike')
    img3 = models.ImageField(upload_to='slike', blank=True, null=True,
                               verbose_name='Slike')
    img4 = models.ImageField(upload_to='slike', blank=True, null=True,
                               verbose_name='Slike')

    def __str__(self):
        return (str(self.ime) + "," + str(self.tipprostora))
    class Meta:
        verbose_name_plural = 'Prostori'


list_vrsta_prijavitelja = [
    ('', ''),
    ('Fizička osoba', 'Fizička osoba'),
    ('Neprofitna udruga', 'Neprofitna udruga'),
    ('Pravna osoba', 'Pravna osoba'),
    ('Ostalo', 'Ostalo'),
]

class Rezervacija(models.Model):
    vrsta_prijavitelja = models.CharField(max_length=50, null=True, blank=True, choices=list_vrsta_prijavitelja, verbose_name='Vrsta prijavitelja')
    naziv = models.CharField(max_length=60, verbose_name= 'Ime i prezime (za fizičke osobe) \nili naziv društva (za pravne osobe)')
    sjediste = models.CharField(max_length=120, verbose_name= 'Prebivalište (za fizičke osobe) \nili sjedište (za pravne osobe)')
    zastupnik = models.CharField(max_length=60, verbose_name= 'Ime i prezime osobe ovlaštene za zastupanje (samo za pravne osobe)')
    oib_mbs = models.CharField(max_length=60, verbose_name= 'OIB ili MBS (za pravne osobe)')
    email = models.EmailField(blank=False, verbose_name='E-mail')
    opis_aktivnosti = models.CharField(max_length=120, verbose_name= 'Opis aktivnosti koja bi se obavljala u prostoru')
    gradska_cetvrt = models.ForeignKey(GradskaCetvrt,on_delete=models.CASCADE, verbose_name='Gradska četvrt')
    mjesni_odbor = models.ForeignKey(MjesniOdbor, on_delete=models.CASCADE, verbose_name='Mjesni odbor')
    prostor = models.ForeignKey(Prostor, on_delete=models.CASCADE, verbose_name='Prostor')
    datum = models.DateField(default=date.today(), blank=False, null=False)
    vrijeme_pocetak = models.TimeField(blank=False)
    vrijeme_kraj = models.TimeField(blank=False)
    napomena = models.CharField(max_length=120, verbose_name= 'Napomena')
    status = models.BooleanField(default=False)
    prilog1 = models.FileField(upload_to='prilozi', blank=True, verbose_name='Prilog 1')
    prilog2 = models.FileField(upload_to='prilozi', blank=True, verbose_name='Prilog 2')
    prilog3 = models.FileField(upload_to='prilozi', blank=True, verbose_name='Prilog 3')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Kreirano')

    def __str__(self):
        return (str(self.naziv) + ", " + str(self.opis_aktivnosti) + "," + str(self.datum))
    class Meta:
        verbose_name_plural = 'Rezervacije'

class Predsjednik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Username')
    ime = models.CharField(max_length=60, verbose_name='Ime i Prezime')
    funkcija = models.CharField(max_length=60, verbose_name='Funkcija')
    email = models.EmailField(blank=False, verbose_name='E-mail')
    mjesni_odbor = models.ForeignKey(MjesniOdbor, on_delete=models.CASCADE, verbose_name='Mjesni odbor')

    def __str__(self):
        return (str(self.ime) + ", " + str(self.mjesni_odbor))

    class Meta:
        verbose_name_plural = 'Predsjednici'