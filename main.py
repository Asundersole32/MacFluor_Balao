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
    else:
        return False


def kilogram_to_newton(weight):
    newton = weight/0.10197
    return newton


def add_persons(persons_newton, load):
    new_load = persons_newton + load
    return new_load


def main():
    diameter = float(input("Insert the diameter of the balloon: "))
    load = float(input("Insert the balloon's load: "))
    gravity = float(input("Insert the gravity: "))
    atmosphere_pressure = float(input("Insert the atmosphere pressure: "))
    temperature = float(input("Insert the atmosphere temperature: "))
    temp_scale = input("Insert the temperature scale(Celsius, Kelvin or Fahrenheit): ")
    temp_scale = temp_scale.lower()

    converted_temp = temp_converter(temperature, temp_scale)

    if not converted_temp:
        print("Type a acceptable scale!")
        return main()

    choice1 = input("Do you want to add persons on the balloon?(yes or no): ")
    choice1 = choice1.lower()

    if choice1 == "yes":
        persons_weight = float(input("Insert the persons weight(in kilograms): "))
        persons_newton = kilogram_to_newton(persons_weight)
        new_load = add_persons(persons_newton, load)
        air_temp = activity_2(diameter, new_load, converted_temp, gravity, atmosphere_pressure)
        return air_temp
    elif choice1 == "no":
        air_temp = activity_2(diameter, load, converted_temp, gravity, atmosphere_pressure)
        return air_temp
    else:
        print("Please, answer with yes or no!")
        return main()

    choice2 = input("Do you want to change the balloon diameter?(yes or no): ")
    choice2 = choice2.lower()

    if choice2 == "yes":
        new_diameter = float(input("Please, insert the new diameter: "))
        air_temp = activity_2(new_diameter, new_load, converted_temp, gravity, atmosphere_pressure)
    elif choice2 == "no":
        air_temp = activity_2(diameter, load, converted_temp, gravity, atmosphere_pressure)
        return air_temp
    else:
        print("Please, answer with yes or no!")
        return main()


main()
