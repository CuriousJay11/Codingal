countries = {'India': '0091', 'Australia': '0025', 'Nepal': '00977'}

country = input("Enter the country name: ")
if country in countries:
    print(f"The country code for {country} is {countries[country]}")
else:
    print("Sorry, country not found in the dictionary.")