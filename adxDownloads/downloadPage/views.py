from django.http import FileResponse
from django.shortcuts import render
import os

# Create your views here.
def index(request):
    charts = {}
    
    VERSION = "PRISM PLUS"
    for zipName in os.listdir(f"downloadPage/static/charts/{VERSION}"):
        chartName = zipName.split(".zip")[0]
        charts[chartName] = ""     
    for imageName in os.listdir(f"downloadPage/static/images"):
        charts[imageName.split(".")[0]] = (f"images/{imageName}")

    return render(request, "index.html", {"charts": charts})

def download(request, name):
    print(name)
    return FileResponse(open(f"downloadPage/static/charts/PRISM PLUS/{name}.zip", 'rb'))