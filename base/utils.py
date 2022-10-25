from .models import Vehicle


def validateData(data):
    if (
        "model_year" not in data
        or "make" not in data
        or "model" not in data
        or "rejection_percentage" not in data
        or "reason_1" not in data
        or "reason_2" not in data
        or "reason_3" not in data
    ):
        return 0
    else:
        return 1


def updateData(car, inst):
    car.update(model_year=inst["model_year"])
    car.update(make=inst["make"])
    car.update(model=inst["model"])
    car.update(rejection_percentage=inst["rejection_percentage"])
    car.update(reason_1=inst["reason_1"])
    car.update(reason_2=inst["reason_2"])
    car.update(reason_3=inst["reason_3"])


def getCar(model_year, make, model):
    carData = Vehicle.objects.filter(
        model_year=model_year, make=make, model=model
    ).values()
    return carData
