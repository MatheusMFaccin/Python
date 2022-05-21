from car import Car,Corsa


make = input("who make this car ? ")
model = input("what is the car model ? ")
year = input("What is the year of manufacture for car ? ")
color = input("what is the color of the car ? ")

car1 = Car(make,model,year,color)

print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)

car1.drive()

print(car1.sound())

corsa = Corsa()

print(corsa.sound())