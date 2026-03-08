Hours = int(input(" Number of Hours : " ))
vehicle = int(input("Vehicle type (Bike:1, Car/Van/SUV/Cab/Threewheel:2, Lorry/Bus:3): "))
day = int(input("Day (Monday:1 ... Sunday:7): "))

#Normal Rate
if vehicle == 1:
    rate = 100
    vtype = "Bike"
elif vehicle == 2:
    rate = 200
    vtype = "Car"
else:
    rate = 400
    vtype = "Bus/Lorry"

#Weekend Rate
if day == 6 or day == 7:
    rate = rate * 1.5
    day_type = "Weekends"
else:
    day_type = "Weekdays"

total = Hours * rate
discount_1 =0
total_discount1 =0

if Hours == 1:
    total = 0

if Hours > 5:
    add_hours = Hours -5
    discount_1 = 0.01 * add_hours
    discount_1 = min(discount_1,0.1)
    total_discount1= total * discount_1


# Output
print(f"\n{vtype}s are charged Rs.{int(rate)} per hour on {day_type}")
print("\nNumber of hours:",Hours,"hrs")
print("\nRate per hour : Rs.",rate)
print("\nTotal before discount:",total)
if Hours == 1:
    print("\n For under 1 hour parking is free")
if Hours > 5 :
    print("\n discount over 5 hours (max 10%) :",discount_1*100,"%","Rs.",total_discount1 )
print("\nTotal:",total-total_discount1)
