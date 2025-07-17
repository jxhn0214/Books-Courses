def prnt_car_info(manufacturer, model, **car_information):
    car_information['manufacturer'] = manufacturer
    car_information['model'] = model
    return car_information

car_information = {}
GR86_info = prnt_car_info('toyota', 'gr86', drive_train="RWD", MSRP='$30,000')
print(GR86_info)


