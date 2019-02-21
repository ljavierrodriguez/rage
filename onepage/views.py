from django.shortcuts import render

# Create your views here.
from onepage.models import General, AboutDescription


def home(request, template_name="index.html"):

    general = General.objects.first()
    aboutDescription = AboutDescription.objects.all()

    context = {
        "general": general,
        "descriptions": aboutDescription
    }

    return render(request, template_name, context)