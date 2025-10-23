planet = input("Pick a Planet: ").lower()
gravity = 0.0
if planet == "mars" or planet == "mercury":
    gravity = 3.7
elif planet == "venus":
    gravity = 8.9
elif planet == "jupiter":
    gravity = 23.1
elif planet == "saturn":
    gravity = 9
elif planet == "uranus":
    gravity = 8.7
elif planet == "neptune":
    gravity = 11
else:
    print("Unrecognized Planet.")

if gravity:
    earth_weight = float(input("How much does it weigh on Earth(kg)? "))
    earth_gravity = 9.81
    mass = earth_weight/earth_gravity
    new_weight = round(mass * gravity, 1)

    print("It would weigh " + str(new_weight) + " kg on " + planet + ".")