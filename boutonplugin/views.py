from django.shortcuts import get_object_or_404, render
from .models import Url

def index ( request ):

    url = get_object_or_404(Url, pk=1)
    return render(request, 'boutonplugin/index.html', {'test': url})