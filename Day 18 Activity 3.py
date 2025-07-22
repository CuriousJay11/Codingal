def hotel_cost(nights):
    return 200* nights

def plane_ride_cost(city):
    if "Mumbai" == city:
        return 183
    elif "Chennai" == city:
        return 220
    elif "Dehli" == city:
        return 50
    elif "Bangalore" == city:
        return 200
    
def car_rental_cost(Days):
    if "10" == Days:
        return 300
    elif "15" == Days:
        return 375
    elif "20" == Days:
        return 445
    elif "30" == Days:
        return 625
    
def trip_cost(city,nights,Days):
    return car_rental_cost(Days) + hotel_cost(nights) + plane_ride_cost(city)


print("The total hotel cost is", hotel_cost(10))
print("The total plane cost is", plane_ride_cost("Mumbai"))
print("The total car rental cost is", car_rental_cost("15"))
print("The total cost",(trip_cost))


