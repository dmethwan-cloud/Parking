Hours = int(input(" Number of Hours : " ))
vehicle = int(input("Vehicle type (Bike:1, Car/Van/SUV/Cab/Threewheel:2, Lorry/Bus:3): "))
if vehicle == 1:
    rate = 100
    vtype = "Bike"
elif vehicle == 2:
    rate = 200
    vtype = "Car"
else:
    rate = 400
    vtype = "Bus/Lorry"

total = Hours * rate
print ( " Your Total Bill :" ,total)