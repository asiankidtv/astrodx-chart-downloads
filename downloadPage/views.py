from django.http import FileResponse
from django.shortcuts import render
import os
from zipfile import ZipFile

# Create your views here.
def index(request):
    # Switch system to dictionary in future..?
    charts = {}
    #imagePaths = []
    
    VERSION = "PRISM PLUS"
    for zipName in os.listdir(f"downloadPage/static/charts/{VERSION}"):
        chartName = zipName.split(".zip")[0]
        charts[chartName] = ""
        #charts.append(chartName)
        #imagePaths[chartName] = ""
        

    for imageName in os.listdir(f"downloadPage/static/images"):
        #imagePaths[imageName.split(".")[0]] = (f"images/{imageName}")
        charts[imageName.split(".")[0]] = (f"images/{imageName}")

    return render(request, "index.html", {"charts": charts})

def download(request):
    # Todo:
        # Write Python Script that takes the raw gdrive folders and converts them to zips of appropiate name
        # In the index function, for every chart wanted, unzip file and pass the bg image file to index.html
            # If needed check if bg.png or bg.jpg exists and return that
        # Based on query parameter, return the corresponding zip file to the client.
    return FileResponse(open("downloadPage/static/charts/PRISM PLUS/AFTER PANDORA.zip", 'rb'))