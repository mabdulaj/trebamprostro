from django.contrib import admin
from django.utils.html import format_html
from admin_numeric_filter.admin import NumericFilterModelAdmin, SingleNumericFilter, RangeNumericFilter, \
    SliderNumericFilter

from django.urls import reverse
from django.http import HttpResponseRedirect

from django.views.generic.edit import FormView

from .models import Grad, GradskaCetvrt, MjesniOdbor, TipProstora, Prostor, Rezervacija, Predsjednik

@admin.action(description="Rezervacija")
def create_form(modeladmin, request, queryset):

    # Get the primary keys of the selected objects
    selected_ids = queryset.values_list('pk', flat=True)

    # Redirect to the form view with the selected IDs as parameters
    url = reverse('assets:rezervacija', args=selected_ids)

    return HttpResponseRedirect(url)

create_form.short_description = "Open Form View in New Tab"


class CustomSliderNumericFilter(SliderNumericFilter):
    MAX_DECIMALS = 2
    STEP = 10
# Register your models here.

class GradAdmin(admin.ModelAdmin):
    list_display = ['ime_grada', 'zipcode', 'drzava', 'latitude', 'longitude']

class GradskaCetvrtAdmin(admin.ModelAdmin):
    list_display = ['ime', 'grad']

class MjesniOdborAdmin(admin.ModelAdmin):
    list_display = ['ime', 'broj', 'address', 'gradska_cetvrt', 'latitude', 'longitude']

class TipProstoraAdmin(admin.ModelAdmin):
    list_display = ['ime']

class ProstorAdmin(admin.ModelAdmin):
    list_display = ['ime', 'tipprostora', 'povrsina', 'mjesniodbor', 'address'
                    , 'sanitarni', 'grijanje', 'klima', 'wifi']
    list_filter = ['tipprostora', 'mjesniodbor__gradska_cetvrt__ime', 'sanitarni','grijanje','klima','wifi', 'povrsina']
    actions = [create_form]


class RezervacijaAdmin(admin.ModelAdmin):
    list_display = ['naziv', 'sjediste', 'zastupnik', 'oib_mbs', 'email', 'opis_aktivnosti',
                    'prostor', 'datum', 'vrijeme_pocetak', 'vrijeme_kraj', 'status' ,'date_created']

class PredsjednikAdmin(admin.ModelAdmin):
    list_display = ['user', 'ime', 'funkcija', 'email', 'mjesni_odbor']

admin.site.register(Grad, GradAdmin)
admin.site.register(GradskaCetvrt, GradskaCetvrtAdmin)
admin.site.register(MjesniOdbor, MjesniOdborAdmin)
admin.site.register(TipProstora, TipProstoraAdmin)
admin.site.register(Prostor, ProstorAdmin)
admin.site.register(Rezervacija, RezervacijaAdmin)
admin.site.register(Predsjednik, PredsjednikAdmin)

