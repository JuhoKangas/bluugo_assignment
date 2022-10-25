from fileinput import filename
from django.shortcuts import render
from .forms import FileForm
from .models import Vehicle
import json
from .utils import *

# Create your views here.


def index(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = json.load(request.FILES["file"])
            for inst in file:
                if validateData(inst):
                    checkCar = getCar(inst["model_year"], inst["make"], inst["model"])
                    if checkCar:
                        updateData(checkCar, inst)
                    else:
                        newData = Vehicle(
                            model_year=inst["model_year"],
                            make=inst["make"],
                            model=inst["model"],
                            rejection_percentage=inst["rejection_percentage"],
                            reason_1=inst["reason_1"],
                            reason_2=inst["reason_2"],
                            reason_3=inst["reason_3"],
                        )
                        newData.save()
    else:
        form = FileForm()
    json_data = json.dumps(list(Vehicle.objects.values()))

    return render(request, "index.html", {"form": form, "json_data": json_data})
