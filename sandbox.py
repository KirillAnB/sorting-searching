import datetime


def get_date():
    today = datetime.datetime.today()
    day = str(today.date())
    print(type(day))
    return day


def bike_base(model, bought_day = get_date()):
    new_bike = {
        'model': model,
        "date" : bought_day
    }
    return new_bike

Honda = bike_base('Super cub')
print(Honda)
