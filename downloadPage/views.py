from django.http import FileResponse
from django.shortcuts import render
import os
from zipfile import ZipFile

# Create your views here.
def index(request):
    charts = []
    for chartName in os.listdir("downloadPage/static/charts/PRiSM PLUS"):
        charts.append(os.path.join("downloadPage/static/charts/PRiSM PLUS", chartName))
    return render(request, "index.html")

def download(request):
    return FileResponse(open("downloadPage/static/charts/AFTER PANDORA.zip", 'rb'))