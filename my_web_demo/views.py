from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
import os
from django.conf import settings
# from .models import Product
# views.py (write logic using those models)
# views.py (write logic using those models)

# Create your views here.
def Home(request):
    return render(request=request, template_name='home.html')


