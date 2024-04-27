def activity_2(diameter, load, temp, gravity, atmosphere_pressure):
    air_pressure = atmosphere_pressure - ((6*load)/(gravity*3.14*(diameter**3)))
    print("The hot air pressure is: ", air_pressure)
    temp_air = ((temp*atmosphere_pressure)/air_pressure)
    print("The hot air temperature is: ", temp_air)
    return [air_pressure, temp_air]


def temp_converter(temp, temp_scale):
    if temp_scale == 'fahrenheit':
        converted_temp = ((temp - 32) * (5/9)) + 273
        return converted_temp
    elif temp_scale == 'celsius':
        converted_temp = temp + 273
        return converted_temp
    elif temp_scale == 'kelvin':
        return temp


diameter = float(input("Insert de diameter of the balloon: "))
load = float(input("Insert the balloon's load: "))
temperature = float(input("Insert the atmosphere temperature: "))
temp_scale = input("Insert the temperature scale(Celsius, Kelvin or Fahrenheit): ")
temp_scale = temp_scale.lower()
gravity = float(input("Insert the gravity: "))
atmosphere_pressure = float(input("Insert the atmosphere pressure: "))

converted_temp = temp_converter(temperature, temp_scale)
air_temp = activity_2(diameter, load, converted_temp, gravity, atmosphere_pressure)
