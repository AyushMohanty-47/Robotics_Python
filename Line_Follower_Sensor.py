def get_sensor_values():
    values = input("Enter 6 sensor values: ")

    sensors=list(map(int,values))

    active=len(list(filter(lambda x: x == 1,sensors)))

    return sensors,active