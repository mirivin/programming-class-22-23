# Amir Valizadeh
# This calculator takes your weight that you input (in pounds) and converts it to what your weight would be if you were on [other planet in our solar system]


import math

print("Please input your weight in pounds and i will return what your    weight would be on the Moon, and every planet in our solar system!")
weight = int(input())
earth_force_of_gravity = 9.81
weight_on_moon = (weight / earth_force_of_gravity) * 1.622
weight_on_jupiter = (weight / earth_force_of_gravity) * 24.79
weight_on_saturn = (weight / earth_force_of_gravity) * 10.44
weight_on_mars = (weight / earth_force_of_gravity) * 3.711
weight_on_mercury = (weight / earth_force_of_gravity) * 3.7
weight_on_venus = (weight / earth_force_of_gravity) * 8.87
weight_on_uranas = (weight / earth_force_of_gravity) * 8.69
weight_on_neptune = (weight / earth_force_of_gravity) * 11.15
print("your weight on the moon is", (weight_on_moon))
print("your weight on Jupiter is", (weight_on_jupiter))
print("your weight on Saturn is", (weight_on_saturn))
print("your weight on Mars is", (weight_on_mars))
print("your weight on Mercury is", (weight_on_mercury))
print("your weight on Venus is", (weight_on_venus))
print("your weight on Uranas is", (weight_on_uranas))
print("your weight on Neptune is", (weight_on_neptune))
