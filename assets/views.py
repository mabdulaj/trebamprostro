from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from .models import Prostor
from .models import MjesniOdbor
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index_page(request):
    context = {}
    return render(request, 'index.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def prostori_page(request):
    if request.method == 'POST':
        sanitarni = request.POST.get('sanitarni')
        grijanje = request.POST.get('grijanje')
        klima = request.POST.get('klima')
        filter = Prostor.objects.filter(Q(sanitarni=sanitarni) | Q(grijanje=grijanje) | Q(klima=klima))
        context = {'prostori': filter}
        return render(request, 'prostori.html', context)
    else:
        all_prostori_list = Prostor.objects.all().order_by('-id')



    paginator = Paginator(all_prostori_list, 10)
    page = request.GET.get('page')
    all_prostori = paginator.get_page(page)
    context = {'prostori': all_prostori}

    return render(request, 'prostori.html',context)

from django.shortcuts import render, get_object_or_404
from .models import Rezervacija
from .forms import RezervacijaForm  # Import your form

def your_form_view(request, *args):
    # Extract the object IDs from the URL parameters
    object_ids = [int(arg) for arg in args]

    # Filter the queryset based on the object IDs
    queryset = Rezervacija.objects.filter(pk__in=object_ids)

    # Use the queryset to initialize the form
    form = RezervacijaForm(queryset)

    return render(request, 'rezervacija.html', {'form': form})