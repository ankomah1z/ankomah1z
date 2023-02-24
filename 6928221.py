# list of available cars and their prices
cars = {
'Bugatti' : 50000,
'Ferrari' : 47000,
'Toyota' : 64000,
'Lexus' : 2000,
'Mazda' : 56778,
'Ford' : 90000,
'Jeep' : 34000,
'Chevrolet' : 70000,
'Tesla' : 59000,
'Hyundai' : 80000,
'Lamborghini' : 10000,
'Mini' : 20000,
'Alfa Romeo' : 200000,
'Audi' : 49000,
'Mitsubishi' : 70000,
'Volvo' : 60000,
'Honda' : 80000,
'Bentley' :56598990,
'Maserati' : 800000,
'Jaguar' : 500000,
'Land rover' : 900000,
'Lincoln' : 70000,
'Rolls-Royce phantom' : 58900,
'Acura' : 600000,
'Infiniti' :60000,
'BMW' : 700000000,
'Cadillac' : 800000,
'Kia' : 577786,
'Saturn' : 678888,
'Aston Martin' : 966647
}  
car_name = input("Enter a car_name: ")
if car_name in cars:
    print("Yes Your car is available")
    car_price = cars[car_name]
    print(f"The price of {car_name} is ${car_price}.")
else:   
    print(f"Sorry,{car_name} is not available") 